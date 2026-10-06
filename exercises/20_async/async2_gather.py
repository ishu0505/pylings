"""
async2_gather — Concurrent execution with asyncio.gather   difficulty: easy

Implement:
`async def fetch_all_users(user_ids: list[str]) -> list[str]`:
- fetches greetings for all user_ids concurrently using `asyncio.gather`.
- returns list of greetings in the same order as user_ids.
"""

# I AM NOT DONE

# Concept Tip: Running 10 requests concurrently with gather takes as long as the single slowest request, not the sum of all 10.
import asyncio


async def fetch_single(user_id: str) -> str:
    await asyncio.sleep(0.02)
    return f"User:{user_id}"


async def fetch_all_users(user_ids: list[str]) -> list[str]:
    # TODO: implement concurrently with asyncio.gather
    raise NotImplementedError


# ---------------------------------------------------------------- tests
import time


def test_fetch_all_concurrent():
    users = ["u1", "u2", "u3", "u4"]
    t0 = time.perf_counter()
    res = asyncio.run(fetch_all_users(users))
    elapsed = time.perf_counter() - t0

    assert res == ["User:u1", "User:u2", "User:u3", "User:u4"]
    # 4 requests with 0.02s each would take 0.08s sequentially, but < 0.06s concurrently
    assert elapsed < 0.06
