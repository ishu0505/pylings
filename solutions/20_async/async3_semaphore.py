"""
async3_semaphore — Solution
"""
import asyncio

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
    sem = asyncio.Semaphore(max_concurrency)

    async def worker(p: str) -> str:
        async with sem:
            return await mock_llm_call(p)

    return list(await asyncio.gather(*(worker(p) for p in prompts)))


# ---------------------------------------------------------------- tests


def test_semaphore_limits():
    global peak_concurrency, current_concurrency
    peak_concurrency = current_concurrency = 0

    prompts = [f"p{i}" for i in range(6)]
    res = asyncio.run(capped_fetch_all(prompts, max_concurrency=2))

    assert len(res) == 6
    assert peak_concurrency <= 2
