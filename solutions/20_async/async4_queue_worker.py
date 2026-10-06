"""
async4_queue_worker — Solution
"""
import asyncio


async def run_worker_pool(tasks: list[int], num_workers: int = 2) -> list[int]:
    q: asyncio.Queue[int] = asyncio.Queue()
    for t in tasks:
        q.put_nowait(t)

    results: list[int] = []

    async def worker() -> None:
        while True:
            try:
                item = q.get_nowait()
            except asyncio.QueueEmpty:
                break
            await asyncio.sleep(0.005)
            results.append(item * 2)
            q.task_done()

    workers = [asyncio.create_task(worker()) for _ in range(num_workers)]
    await asyncio.gather(*workers)
    return results


# ---------------------------------------------------------------- tests


def test_worker_pool():
    items = [1, 2, 3, 4, 5]
    results = asyncio.run(run_worker_pool(items, num_workers=2))
    assert sorted(results) == [2, 4, 6, 8, 10]
