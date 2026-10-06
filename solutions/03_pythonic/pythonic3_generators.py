"""
pythonic3_generators — Solution
"""
from typing import Any, Iterator


def fibonacci_stream(limit: int) -> Iterator[int]:
    a, b = 0, 1
    while a < limit:
        yield a
        a, b = b, a + b


def chunked(iterable: Any, chunk_size: int) -> Iterator[list[Any]]:
    batch = []
    for item in iterable:
        batch.append(item)
        if len(batch) == chunk_size:
            yield batch
            batch = []
    if batch:
        yield batch


# ---------------------------------------------------------------- tests


def test_fibonacci_stream():
    assert list(fibonacci_stream(20)) == [0, 1, 1, 2, 3, 5, 8, 13]
    assert list(fibonacci_stream(1)) == [0]


def test_chunked():
    data = [1, 2, 3, 4, 5, 6, 7]
    assert list(chunked(data, 3)) == [[1, 2, 3], [4, 5, 6], [7]]
    assert list(chunked([], 3)) == []
    assert list(chunked(range(4), 2)) == [[0, 1], [2, 3]]
