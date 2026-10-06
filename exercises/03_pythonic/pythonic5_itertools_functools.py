"""
pythonic5_itertools_functools — Advanced itertools & caching   difficulty: medium

1. `consecutive_counts(s: str) -> list[tuple[str, int]]`:
   counts consecutive identical characters using itertools.groupby: e.g. "aaabbc" -> [("a", 3), ("b", 2), ("c", 1)].
2. `memoized_factorial(n: int) -> int`:
   computes factorial of n using recursion and functools.lru_cache.
"""

# I AM NOT DONE

# Concept Tip: `groupby` groups consecutive matching elements like a run-length encoder.
from functools import lru_cache
from itertools import groupby


def consecutive_counts(s: str) -> list[tuple[str, int]]:
    # TODO: implement
    raise NotImplementedError


def memoized_factorial(n: int) -> int:
    # TODO: implement with @lru_cache
    raise NotImplementedError


# ---------------------------------------------------------------- tests


def test_consecutive_counts():
    assert consecutive_counts("aaabbc") == [("a", 3), ("b", 2), ("c", 1)]
    assert consecutive_counts("a") == [("a", 1)]
    assert consecutive_counts("") == []


def test_memoized_factorial():
    assert memoized_factorial(0) == 1
    assert memoized_factorial(5) == 120
    assert memoized_factorial(10) == 3628800
    # verify cache info exists
    assert hasattr(memoized_factorial, "cache_info")
