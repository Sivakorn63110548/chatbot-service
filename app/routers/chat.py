import json
import re
import logging
from fastapi import APIRouter, WebSocket, WebSocketDisconnect, Query
from app.core.config import ACCESS_TOKEN
from app.core.database import save_message, load_history
from app.services.llm import get_chat_response

logger = logging.getLogger("chat")
router = APIRouter()


@router.websocket("/ws/chat")
async def websocket_chat(
    websocket: WebSocket,
    token: str = Query(...),
    session_id: str = Query(...),
):
    if token != ACCESS_TOKEN:
        await websocket.close(code=1008)
        logger.warning(f"[WS] Unauthorized from {websocket.client.host}")
        return

    await websocket.accept()
    client = websocket.client
    logger.info(f"[WS] Connected: {client.host}:{client.port} session={session_id}")

    history = load_history(session_id)
    logger.info(f"[WS] Loaded {len(history)} messages from DB")

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

            save_message(session_id, "user", user_message)
            history.append({"role": "user", "content": user_message})

            response = get_chat_response(history)
            response = re.sub(r"<think>.*?</think>", "", response, flags=re.DOTALL).strip()

            save_message(session_id, "assistant", response)
            history.append({"role": "assistant", "content": response})

            logger.info(f"[WS] Reply to {client.host}: {response[:80]}...")
            await websocket.send_json({"message": response})

    except WebSocketDisconnect:
        logger.info(f"[WS] Disconnected: {client.host}:{client.port} session={session_id}")
