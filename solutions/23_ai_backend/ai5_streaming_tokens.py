"""
ai5_streaming_tokens — Solution
"""
from fastapi import FastAPI
from fastapi.responses import StreamingResponse
from pydantic import BaseModel
from fastapi.testclient import TestClient

app = FastAPI()


class StreamRequest(BaseModel):
    prompt: str


def generate_tokens(prompt: str):
    words = ["Hello", "World", "from", "FastAPI"]
    for w in words:
        yield f"data: {w}\n\n"
    yield "data: [DONE]\n\n"


@app.post("/stream-generate")
def stream_generate(req: StreamRequest):
    return StreamingResponse(generate_tokens(req.prompt), media_type="text/event-stream")


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
