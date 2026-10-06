"""
async4_queue_worker — Worker Pool with asyncio.Queue    difficulty: medium

Implement `run_worker_pool(tasks: list[int], num_workers: int = 2) -> list[int]`:
- puts all tasks (integers) into an `asyncio.Queue`
- spawns `num_workers` worker coroutines that take tasks, multiply them by 2, and append to a shared results list
- gracefully cancels or stops workers when queue is empty and joins
- returns results
"""

# I AM NOT DONE

# Concept Tip: `asyncio.Queue` coordinates work across concurrent consumer coroutines.
import asyncio


async def run_worker_pool(tasks: list[int], num_workers: int = 2) -> list[int]:
    # TODO: implement
    raise NotImplementedError


# ---------------------------------------------------------------- tests


def test_worker_pool():
    items = [1, 2, 3, 4, 5]
    results = asyncio.run(run_worker_pool(items, num_workers=2))
    assert sorted(results) == [2, 4, 6, 8, 10]
