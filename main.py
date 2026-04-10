import logging
import fastapi
import uvicorn
from contextlib import asynccontextmanager
from dotenv import load_dotenv

load_dotenv()

logging.basicConfig(level=logging.INFO, format="%(levelname)s:     %(message)s")

from fastapi.middleware.cors import CORSMiddleware
from app.routers.chat import router as chat_router
from app.routers.history import router as history_router
from app.core.database import init_db, check_connection
from app.core.config import ALLOWED_ORIGIN


@asynccontextmanager
async def lifespan(_: fastapi.FastAPI):
    log = logging.getLogger("main")
    try:
        check_connection()
        log.info("[DB] Connected successfully")
        init_db()
        log.info("[DB] Tables ready")
    except Exception as e:
        log.error(f"[DB] Connection failed: {e}")
        raise
    yield


app = fastapi.FastAPI(lifespan=lifespan)

app.add_middleware(
    CORSMiddleware,
    allow_origins=[ALLOWED_ORIGIN],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(chat_router)
app.include_router(history_router)


@app.get("/", status_code=200)
def read_root():
    return {"message": "BookDev Chatbot Service is running!"}


@app.get("/health", status_code=200)
def read_health():
    db_ok = True
    try:
        check_connection()
    except Exception:
        db_ok = False

    return {
        "status": "healthy" if db_ok else "degraded",
        "services": {
            "api": True,
            "database": db_ok,
        },
    }


if __name__ == "__main__":
    uvicorn.run(app, host="localhost", port=8000)
