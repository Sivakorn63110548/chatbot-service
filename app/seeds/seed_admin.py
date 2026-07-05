"""
Create initial admin user.
Usage: python -m app.seeds.seed_admin <username> <password>
"""
import sys, os
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.dirname(__file__))))

from dotenv import load_dotenv
load_dotenv()

from sqlalchemy import text
from app.core.database import engine
from app.services.auth import hash_password


def create_admin(username: str, password: str) -> None:
    with engine.begin() as conn:
        existing = conn.execute(
            text("SELECT id FROM admin_users WHERE username = :u"),
            {"u": username},
        ).fetchone()

        if existing:
            conn.execute(
                text("UPDATE admin_users SET password_hash = :h WHERE username = :u"),
                {"h": hash_password(password), "u": username},
            )
            print(f"Updated password for '{username}'.")
        else:
            conn.execute(
                text("INSERT INTO admin_users (username, password_hash) VALUES (:u, :h)"),
                {"u": username, "h": hash_password(password)},
            )
            print(f"Admin user '{username}' created.")


if __name__ == "__main__":
    if len(sys.argv) != 3:
        print("Usage: python -m app.seeds.seed_admin <username> <password>")
        sys.exit(1)
    create_admin(sys.argv[1], sys.argv[2])
