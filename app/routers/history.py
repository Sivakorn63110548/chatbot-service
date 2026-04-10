import logging
from fastapi import APIRouter, Query, HTTPException
from app.core.config import ACCESS_TOKEN
from app.core.database import load_history

logger = logging.getLogger("history")
router = APIRouter()


@router.get("/history")
def get_history(
    session_id: str = Query(...),
    token: str = Query(...),
):
    if token != ACCESS_TOKEN:
        raise HTTPException(status_code=401, detail="Unauthorized")

    messages = load_history(session_id)

    return {
        "session_id": session_id,
        "count": len(messages),
        "messages": messages,
    }
