"""
pythonic3_generators — Generator functions & chunking   difficulty: medium

Implement:
1. `fibonacci_stream(limit: int)`:
   generates Fibonacci numbers (0, 1, 1, 2, 3, 5, ...) while value < limit.
2. `chunked(iterable, chunk_size: int)`:
   yields successive chunks of size chunk_size as lists. The final chunk may be shorter.
"""

# I AM NOT DONE

# Concept Tip: `yield` freezes function state and hands control back to the caller.
from typing import Any, Iterator


def fibonacci_stream(limit: int) -> Iterator[int]:
    # TODO: implement
    raise NotImplementedError


def chunked(iterable: Any, chunk_size: int) -> Iterator[list[Any]]:
    # TODO: implement
    raise NotImplementedError


# ---------------------------------------------------------------- tests


def test_fibonacci_stream():
    assert list(fibonacci_stream(20)) == [0, 1, 1, 2, 3, 5, 8, 13]
    assert list(fibonacci_stream(1)) == [0]


def test_chunked():
    data = [1, 2, 3, 4, 5, 6, 7]
    assert list(chunked(data, 3)) == [[1, 2, 3], [4, 5, 6], [7]]
    assert list(chunked([], 3)) == []
    assert list(chunked(range(4), 2)) == [[0, 1], [2, 3]]
