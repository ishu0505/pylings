"""
async1_coroutines — Solution
"""
import asyncio


async def simulate_io_latency(delay: float = 0.01) -> None:
    await asyncio.sleep(delay)


async def fetch_user_greeting(user_id: str) -> str:
    await simulate_io_latency(0.01)
    return f"Hello, {user_id}!"


# ---------------------------------------------------------------- tests


def test_fetch_user_greeting():
    result = asyncio.run(fetch_user_greeting("Ada"))
    assert result == "Hello, Ada!"
