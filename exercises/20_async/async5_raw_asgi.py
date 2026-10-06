"""
async5_raw_asgi — Raw ASGI Application                 difficulty: hard

Uvicorn and FastAPI communicate via the ASGI (Asynchronous Server Gateway Interface) standard.
Implement `async def asgi_app(scope: dict, receive, send)`:
- If `scope["type"] != "http"`, return.
- If `scope["path"] == "/health"`, send HTTP 200 with body `b'{"status":"ok"}'` and content-type application/json.
- Otherwise send HTTP 404 with body `b'Not Found'`.
"""

# I AM NOT DONE

# Concept Tip: ASGI passes request scope and two async channels (`receive` and `send`).
import json
import httpx


async def asgi_app(scope: dict, receive, send) -> None:
    # TODO: implement raw ASGI protocol
    raise NotImplementedError


# ---------------------------------------------------------------- tests
import asyncio


def test_asgi_app():
    async def run_test():
        transport = httpx.ASGITransport(app=asgi_app)
        async with httpx.AsyncClient(transport=transport, base_url="http://test") as client:
            resp = await client.get("/health")
            assert resp.status_code == 200
            assert resp.json() == {"status": "ok"}

            resp404 = await client.get("/unknown")
            assert resp404.status_code == 404
            assert resp404.text == "Not Found"

    asyncio.run(run_test())
