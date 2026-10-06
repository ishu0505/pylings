"""
last_stone_weight — Last Stone Weight (NeetCode)       difficulty: easy

You have stones with positive integer weights. Each turn, choose the heaviest two stones x and y (x <= y).
If x == y, both are destroyed. If x != y, stone of weight y - x remains.
Return the weight of the last remaining stone, or 0 if none remain.
Goal: O(n log n) time.
"""

# I AM NOT DONE

# Concept Tip: Negating weights lets you use Python's built-in min-heap as a max-heap.
import heapq


def last_stone_weight(stones: list[int]) -> int:
    # TODO: implement
    raise NotImplementedError


# ---------------------------------------------------------------- tests


def test_last_stone():
    assert last_stone_weight([2, 7, 4, 1, 8, 1]) == 1
    assert last_stone_weight([1]) == 1
    assert last_stone_weight([2, 2]) == 0
