# chatbot-service

AI chatbot backend for [Book's portfolio](https://bookdev-vite-react.vercel.app/). Answers questions about Sivakorn Tanyupak using a Groq LLM, with persistent chat history via PostgreSQL.

## Tech Stack

| Layer     | Technology                           |
|-----------|--------------------------------------|
| Runtime   | Python 3.12                          |
| Framework | FastAPI                              |
| LLM       | Groq (`moonshotai/kimi-k2-instruct`) |
| Database  | PostgreSQL + SQLAlchemy 2.0 ORM      |
| Transport | WebSocket                            |
| Deploy    | Vercel                               |

## Project Structure

```
chatbot-service/
├── main.py                  # FastAPI app, lifespan, CORS, routers
├── AI_CONTEXT.md            # Knowledge base fed to the LLM as context
├── requirements.txt
├── vercel.json
├── runtime.txt              # python-3.12
└── app/
    ├── prompts.py           # System prompt template
    ├── core/
    │   ├── config.py        # Env vars
    │   └── database.py      # SQLAlchemy engine, ChatMessage model, DB helpers
    ├── routers/
    │   ├── chat.py          # WebSocket endpoint /ws/chat
    │   └── history.py       # REST endpoint GET /history
    └── services/
        └── llm.py           # Groq client wrapper
```

## API

### WebSocket — `/ws/chat`

```
ws://host/ws/chat?token=<ACCESS_TOKEN>&session_id=<session>
```

**Send:**
```json
{ "message": "What tech stack does Book use?" }
```

**Receive:**
```json
{ "message": "Book uses React, NestJS, FastAPI, PostgreSQL..." }
```

Closes with code `1008` if the token is invalid.

---

### GET `/history`

```
GET /history?token=<ACCESS_TOKEN>&session_id=<session>
```

**Response:**
```json
{
  "session_id": "abc123",
  "count": 4,
  "messages": [
    { "role": "user", "content": "..." },
    { "role": "assistant", "content": "..." }
  ]
}
```

---

### GET `/health`

```json
{
  "status": "healthy",
  "services": { "api": true, "database": true }
}
```

## Environment Variables

Create a `.env` file (local) or set these in Vercel → Project Settings → Environment Variables:

| Variable         | Description                                                                 |
|------------------|-----------------------------------------------------------------------------|
| `GROQ_API_KEY`   | API key from [console.groq.com](https://console.groq.com)                  |
| `POSTGRES_URL`   | PostgreSQL connection string                                                |
| `ACCESS_TOKEN`   | Secret token for WebSocket & history auth                                   |
| `ALLOWED_ORIGIN` | Frontend origin for CORS (e.g. `https://bookdev-vite-react.vercel.app`)    |

## Local Development

```bash
# Install dependencies
pip install -r requirements.txt

# Copy and fill environment variables
cp .env.example .env

# Run the server
python -m uvicorn main:app --reload --port 8000
```

Server starts at `http://localhost:8000`.

## Deploy on Vercel

1. Push to GitHub and import the repo on [vercel.com](https://vercel.com)
2. Set environment variables in **Project Settings → Environment Variables**
3. Vercel detects Python via `runtime.txt` and routes via `vercel.json` automatically

> Requires **Fluid Compute** enabled (default for projects created after April 23, 2025) for WebSocket support.

## Database Schema

```sql
CREATE TABLE chat_messages (
    id         SERIAL PRIMARY KEY,
    session_id TEXT      NOT NULL,
    role       TEXT      NOT NULL,   -- "user" | "assistant"
    content    TEXT      NOT NULL,
    created_at TIMESTAMP DEFAULT NOW()
);
CREATE INDEX idx_session_id ON chat_messages(session_id);
```

Tables are created automatically on startup via `Base.metadata.create_all()`.
