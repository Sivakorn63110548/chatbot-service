from sqlalchemy import create_engine, Column, Integer, String, Text, DateTime, func, text
from sqlalchemy.orm import DeclarativeBase, sessionmaker
from app.core.config import POSTGRES_URL, MAX_HISTORY

_url = POSTGRES_URL.replace("postgres://", "postgresql://", 1)

engine = create_engine(_url, connect_args={"sslmode": "require"}, pool_pre_ping=True)
SessionLocal = sessionmaker(bind=engine)


class Base(DeclarativeBase):
    pass


class ChatMessage(Base):
    __tablename__ = "chat_messages"

    id = Column(Integer, primary_key=True)
    session_id = Column(String, nullable=False, index=True)
    role = Column(String, nullable=False)
    content = Column(Text, nullable=False)
    created_at = Column(DateTime, server_default=func.now())


def check_connection():
    with engine.connect() as conn:
        conn.execute(text("SELECT 1"))


def init_db():
    Base.metadata.create_all(engine)


def save_message(session_id: str, role: str, content: str):
    with SessionLocal() as session:
        session.add(ChatMessage(session_id=session_id, role=role, content=content))
        session.commit()


def load_history(session_id: str) -> list[dict]:
    with SessionLocal() as session:
        rows = (
            session.query(ChatMessage)
            .filter(ChatMessage.session_id == session_id)
            .order_by(ChatMessage.created_at.desc())
            .limit(MAX_HISTORY)
            .all()
        )
        return [{"role": m.role, "content": m.content} for m in reversed(rows)]
