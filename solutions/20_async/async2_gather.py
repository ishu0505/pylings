"""
async2_gather — Solution
"""
import asyncio


async def fetch_single(user_id: str) -> str:
    await asyncio.sleep(0.02)
    return f"User:{user_id}"


async def fetch_all_users(user_ids: list[str]) -> list[str]:
    tasks = [fetch_single(uid) for uid in user_ids]
    return list(await asyncio.gather(*tasks))


# ---------------------------------------------------------------- tests
import time


def test_fetch_all_concurrent():
    users = ["u1", "u2", "u3", "u4"]
    t0 = time.perf_counter()
    res = asyncio.run(fetch_all_users(users))
    elapsed = time.perf_counter() - t0

    assert res == ["User:u1", "User:u2", "User:u3", "User:u4"]
    assert elapsed < 0.06
