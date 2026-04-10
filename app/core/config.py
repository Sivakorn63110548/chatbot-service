import os

GROQ_API_KEY: str = os.environ.get("GROQ_API_KEY", "")
POSTGRES_URL: str = os.environ.get("POSTGRES_URL", "")
ACCESS_TOKEN: str = os.environ.get("ACCESS_TOKEN", "")
MAX_HISTORY: int = 10
LLM_MODEL: str = "moonshotai/kimi-k2-instruct"
LLM_TEMPERATURE: float = 0.3
LLM_MAX_TOKENS: int = 1024
