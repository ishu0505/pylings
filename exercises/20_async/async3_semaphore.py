"""
async3_semaphore — Limiting Concurrency with Semaphore   difficulty: medium

When querying external LLM APIs, sending 100 concurrent requests triggers HTTP 429 rate limits.
Implement `capped_fetch_all(urls: list[str], max_concurrency: int = 2) -> list[str]`:
- limits concurrent active fetches to `max_concurrency` using `asyncio.Semaphore`.
"""

# I AM NOT DONE

# Concept Tip: `asyncio.Semaphore(limit)` allows at most `limit` tasks into the guarded block simultaneously.
import asyncio


# Track peak concurrency for tests
peak_concurrency = 0
current_concurrency = 0


async def mock_llm_call(prompt: str) -> str:
    global peak_concurrency, current_concurrency
    current_concurrency += 1
    peak_concurrency = max(peak_concurrency, current_concurrency)
    await asyncio.sleep(0.02)
    current_concurrency -= 1
    return f"Output for {prompt}"


async def capped_fetch_all(prompts: list[str], max_concurrency: int = 2) -> list[str]:
    # TODO: implement using asyncio.Semaphore and asyncio.gather
    raise NotImplementedError


# ---------------------------------------------------------------- tests


def test_semaphore_limits():
    global peak_concurrency, current_concurrency
    peak_concurrency = current_concurrency = 0

    prompts = [f"p{i}" for i in range(6)]
    res = asyncio.run(capped_fetch_all(prompts, max_concurrency=2))

    assert len(res) == 6
    assert peak_concurrency <= 2
