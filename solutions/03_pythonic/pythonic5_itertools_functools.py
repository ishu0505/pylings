"""
pythonic5_itertools_functools — Solution
"""
from functools import lru_cache
from itertools import groupby


def consecutive_counts(s: str) -> list[tuple[str, int]]:
    return [(char, len(list(group))) for char, group in groupby(s)]


@lru_cache(maxsize=128)
def memoized_factorial(n: int) -> int:
    if n <= 1:
        return 1
    return n * memoized_factorial(n - 1)


# ---------------------------------------------------------------- tests


def test_consecutive_counts():
    assert consecutive_counts("aaabbc") == [("a", 3), ("b", 2), ("c", 1)]
    assert consecutive_counts("a") == [("a", 1)]
    assert consecutive_counts("") == []


def test_memoized_factorial():
    assert memoized_factorial(0) == 1
    assert memoized_factorial(5) == 120
    assert memoized_factorial(10) == 3628800
    assert hasattr(memoized_factorial, "cache_info")
