"""
async1_coroutines — Coroutines and Await               difficulty: easy

Implement:
`async def fetch_user_greeting(user_id: str) -> str`:
- awaits `simulate_io_latency(delay=0.01)`
- returns f"Hello, {user_id}!"
"""

# I AM NOT DONE

# Concept Tip: An async function returns a coroutine object that must be scheduled on the event loop with `await`.
import asyncio


async def simulate_io_latency(delay: float = 0.01) -> None:
    await asyncio.sleep(delay)


async def fetch_user_greeting(user_id: str) -> str:
    # TODO: implement
    raise NotImplementedError


# ---------------------------------------------------------------- tests


def test_fetch_user_greeting():
    result = asyncio.run(fetch_user_greeting("Ada"))
    assert result == "Hello, Ada!"
