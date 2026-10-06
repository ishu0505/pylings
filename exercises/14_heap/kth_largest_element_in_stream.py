"""
kth_largest_element_in_stream — Kth Largest in Stream (NeetCode) difficulty: easy

Design a class to find the kth largest element in a stream.
- `KthLargest(k: int, nums: list[int])`
- `add(val: int) -> int`: appends val and returns the kth largest element.
"""

# I AM NOT DONE

# Concept Tip: A min-heap capped at size k automatically discards elements smaller than the top k.
import heapq


class KthLargest:
    # TODO: implement
    pass


# ---------------------------------------------------------------- tests


def test_kth_largest():
    kl = KthLargest(3, [4, 5, 8, 2])
    assert kl.add(3) == 4   # [2, 3, 4, 5, 8] -> 4
    assert kl.add(5) == 5
    assert kl.add(10) == 5
    assert kl.add(9) == 8
    assert kl.add(4) == 8
