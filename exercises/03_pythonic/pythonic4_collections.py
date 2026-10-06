"""
pythonic4_collections — Specialized collection containers  difficulty: medium

1. `invert_multi_dict(d: dict[str, list[int]]) -> dict[int, list[str]]`:
   Given e.g. {"a": [1, 2], "b": [2, 3]}, returns {1: ["a"], 2: ["a", "b"], 3: ["b"]}
   using collections.defaultdict.
2. `sliding_window_max(nums: list[int], k: int) -> list[int]`:
   Use collections.deque to find the maximum in each sliding window of size k in O(n) time.
"""

# I AM NOT DONE

# Concept Tip: `deque` as a monotonic decreasing queue gives O(1) amortized window max.
from collections import defaultdict, deque


def invert_multi_dict(d: dict[str, list[int]]) -> dict[int, list[str]]:
    # TODO: implement
    raise NotImplementedError


def sliding_window_max(nums: list[int], k: int) -> list[int]:
    # TODO: implement in O(n) using deque
    raise NotImplementedError


# ---------------------------------------------------------------- tests


def test_invert_multi_dict():
    d = {"a": [1, 2], "b": [2, 3]}
    res = invert_multi_dict(d)
    assert res[1] == ["a"]
    assert sorted(res[2]) == ["a", "b"]
    assert res[3] == ["b"]


def test_sliding_window_max():
    nums = [1, 3, -1, -3, 5, 3, 6, 7]
    assert sliding_window_max(nums, 3) == [3, 3, 5, 5, 6, 7]
    assert sliding_window_max([1], 1) == [1]
