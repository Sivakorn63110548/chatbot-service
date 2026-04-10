from groq import Groq
from app.core.config import GROQ_API_KEY, LLM_MODEL, LLM_TEMPERATURE, LLM_MAX_TOKENS, MAX_HISTORY
from app.prompts import SYSTEM_PROMPT, KNOWLEDGE_BASE

client = Groq(api_key=GROQ_API_KEY)


def get_chat_response(messages: list[dict]) -> str:
    system_message = {
        "role": "system",
        "content": SYSTEM_PROMPT.format(context=KNOWLEDGE_BASE),
    }

    response = client.chat.completions.create(
        model=LLM_MODEL,
        messages=[system_message] + messages[-MAX_HISTORY:],
        temperature=LLM_TEMPERATURE,
        max_tokens=LLM_MAX_TOKENS,
        top_p=0.9,
    )

    return response.choices[0].message.content
