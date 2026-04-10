import fastapi
import uvicorn
import logging
from dotenv import load_dotenv
load_dotenv()

logging.basicConfig(level=logging.INFO, format="%(levelname)s:     %(message)s")
from fastapi.middleware.cors import CORSMiddleware
from app.socket import router as socket_router

app = fastapi.FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # ปรับเป็น Vercel domain ตอน deploy
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(socket_router)

@app.get("/", status_code=200)
def read_root():
    return {"Hello": "World"}

@app.get("/health", status_code=200)
def read_health():
    return {"status": "healthy"}

if __name__ == "__main__":
    uvicorn.run(app, host="localhost", port=8000)
