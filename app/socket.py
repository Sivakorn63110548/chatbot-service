import json
import re
import logging
from fastapi import APIRouter, WebSocket, WebSocketDisconnect
from .groq_client import get_chat_response

logger = logging.getLogger("socket")
router = APIRouter()

@router.websocket("/ws/chat")
async def websocket_chat(websocket: WebSocket):
    await websocket.accept()
    client = websocket.client
    logger.info(f"[WS] Connected: {client.host}:{client.port}")
    history: list[dict] = []

    try:
        while True:
            raw = await websocket.receive_text()

            try:
                data = json.loads(raw)
                user_message = data.get("message", "")
            except json.JSONDecodeError:
                user_message = raw

            if not user_message:
                await websocket.send_json({"error": "empty message"})
                continue

            logger.info(f"[WS] Message from {client.host}: {user_message}")

            history.append({"role": "user", "content": user_message})
            response = get_chat_response(history)
            # ตัด <think>...</think> ที่ DeepSeek ใส่มา
            response = re.sub(r"<think>.*?</think>", "", response, flags=re.DOTALL).strip()
            history.append({"role": "assistant", "content": response})

            logger.info(f"[WS] Reply to {client.host}: {response[:80]}...")
            await websocket.send_json({"message": response})

    except WebSocketDisconnect:
        logger.info(f"[WS] Disconnected: {client.host}:{client.port}")
