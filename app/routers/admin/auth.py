import logging
from fastapi import APIRouter, HTTPException, Depends, status
from sqlalchemy import text
from app.core.database import engine
from app.schemas.auth import LoginRequest, TokenResponse, AdminUser
from app.services.auth import verify_password, create_token
from app.dependencies import get_current_admin

logger = logging.getLogger("admin.auth")
router = APIRouter(prefix="/admin", tags=["admin"])


@router.post("/login", response_model=TokenResponse)
def login(body: LoginRequest):
    with engine.connect() as conn:
        row = conn.execute(
            text("SELECT id, password_hash FROM admin_users WHERE username = :u"),
            {"u": body.username},
        ).fetchone()

    if not row or not verify_password(body.password, row.password_hash):
        logger.warning(f"[AUTH] Failed login attempt for '{body.username}'")
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Invalid credentials",
        )

    with engine.begin() as conn:
        conn.execute(
            text("UPDATE admin_users SET last_login = NOW() WHERE id = :id"),
            {"id": row.id},
        )

    logger.info(f"[AUTH] Login: {body.username}")
    return TokenResponse(access_token=create_token(row.id, body.username))


@router.get("/me", response_model=AdminUser)
def me(admin: dict = Depends(get_current_admin)):
    return AdminUser(**admin)


@router.post("/logout", status_code=204)
def logout(admin: dict = Depends(get_current_admin)):
    logger.info(f"[AUTH] Logout: {admin['username']}")
