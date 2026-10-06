"""
top_k_frequent — Top K Frequent Elements (NeetCode)     difficulty: medium

Given an integer array nums and an integer k, return the k most frequent elements.
You must solve it in O(n) time (better than O(n log n)).
"""

# I AM NOT DONE

# Concept Tip: Bucket sort where index represents frequency guarantees O(n) runtime.


def top_k_frequent(nums: list[int], k: int) -> list[int]:
    # TODO: implement in O(n)
    raise NotImplementedError


# ---------------------------------------------------------------- tests


def test_top_k_frequent():
    assert sorted(top_k_frequent([1, 1, 1, 2, 2, 3], 2)) == [1, 2]
    assert top_k_frequent([1], 1) == [1]
    assert sorted(top_k_frequent([4, 1, -1, 2, -1, 2, 3], 2)) == [-1, 2]
