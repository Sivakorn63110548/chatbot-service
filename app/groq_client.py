import os
from groq import Groq
from .data import SYSTEM_PROMPT, KNOWLEDGE_BASE, MAX_HISTORY

client = Groq(api_key=os.environ.get("GROQ_API_KEY"))

def get_chat_response(messages: list[dict]) -> str:
    system_message = {
        "role": "system",
        "content": SYSTEM_PROMPT.format(context=KNOWLEDGE_BASE),
    }

    # จำกัด history ไม่ให้ยาวเกิน
    trimmed = messages[-MAX_HISTORY:]

    response = client.chat.completions.create(
        model="moonshotai/kimi-k2-instruct",
        messages=[system_message] + trimmed,
        temperature=0.3,        # แม่นยำ ไม่เดา
        max_tokens=1024,
        top_p=0.9,
    )

    return response.choices[0].message.content
