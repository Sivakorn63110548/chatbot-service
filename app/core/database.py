import psycopg2
from psycopg2.extras import RealDictCursor
from app.core.config import POSTGRES_URL


def get_conn():
    return psycopg2.connect(POSTGRES_URL)


def check_connection():
    with get_conn() as conn:
        with conn.cursor() as cur:
            cur.execute("SELECT 1")


def init_db():
    with get_conn() as conn:
        with conn.cursor() as cur:
            cur.execute("""
                CREATE TABLE IF NOT EXISTS chat_messages (
                    id SERIAL PRIMARY KEY,
                    session_id TEXT NOT NULL,
                    role TEXT NOT NULL,
                    content TEXT NOT NULL,
                    created_at TIMESTAMP DEFAULT NOW()
                );
                CREATE INDEX IF NOT EXISTS idx_session_id ON chat_messages(session_id);
            """)
            conn.commit()


def save_message(session_id: str, role: str, content: str):
    with get_conn() as conn:
        with conn.cursor() as cur:
            cur.execute(
                "INSERT INTO chat_messages (session_id, role, content) VALUES (%s, %s, %s)",
                (session_id, role, content),
            )
            conn.commit()


def load_history(session_id: str) -> list[dict]:
    with get_conn() as conn:
        with conn.cursor(cursor_factory=RealDictCursor) as cur:
            cur.execute(
                """
                SELECT role, content FROM (
                    SELECT role, content, created_at
                    FROM chat_messages
                    WHERE session_id = %s
                    ORDER BY created_at DESC
                    LIMIT %s
                ) sub ORDER BY created_at ASC
                """,
                (session_id, 10),
            )
            return [{"role": r["role"], "content": r["content"]} for r in cur.fetchall()]
