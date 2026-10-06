"""
async5_raw_asgi — Solution
"""
import httpx


async def asgi_app(scope: dict, receive, send) -> None:
    if scope["type"] != "http":
        return

    path = scope.get("path", "")
    if path == "/health":
        await send({
            "type": "http.response.start",
            "status": 200,
            "headers": [[b"content-type", b"application/json"]],
        })
        await send({
            "type": "http.response.body",
            "body": b'{"status":"ok"}',
        })
    else:
        await send({
            "type": "http.response.start",
            "status": 404,
            "headers": [[b"content-type", b"text/plain"]],
        })
        await send({
            "type": "http.response.body",
            "body": b"Not Found",
        })


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
