"""
ai5_streaming_tokens — Streaming LLM Tokens with SSE    difficulty: medium

To eliminate perceived latency, LLM backends stream tokens via Server-Sent Events (SSE).
Build a FastAPI endpoint:
- `POST /stream-generate`: receives JSON `{"prompt": str}`
- Returns `StreamingResponse` with media_type="text/event-stream"
- Streams each word of the mock generated text as `data: {word}\n\n` followed by `data: [DONE]\n\n`
"""

# I AM NOT DONE

# Concept Tip: SSE streams text chunks over an open HTTP connection using `text/event-stream`.
from fastapi import FastAPI
from fastapi.responses import StreamingResponse
from pydantic import BaseModel
from fastapi.testclient import TestClient

app = FastAPI()

# TODO: implement model and route


# ---------------------------------------------------------------- tests


def test_token_streaming():
    client = TestClient(app)
    response = client.post("/stream-generate", json={"prompt": "Say hello world"})
    assert response.status_code == 200
    assert "text/event-stream" in response.headers["content-type"]

    content = response.text
    assert "data: Hello" in content
    assert "data: World" in content
    assert "data: [DONE]" in content
