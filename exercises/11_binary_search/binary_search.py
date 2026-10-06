"""
binary_search — Binary Search (NeetCode)               difficulty: easy

Given an array of integers nums which is sorted in ascending order, and an integer target,
write a function to search target in nums. If target exists, return its index. Otherwise, return -1.
Goal: O(log n) time.
"""

# I AM NOT DONE

# Concept Tip: `lo + (hi - lo) // 2` avoids integer overflow in low-level languages.


def search(nums: list[int], target: int) -> int:
    # TODO: implement in O(log n)
    raise NotImplementedError


# ---------------------------------------------------------------- tests


def test_binary_search():
    assert search([-1, 0, 3, 5, 9, 12], 9) == 4
    assert search([-1, 0, 3, 5, 9, 12], 2) == -1
    assert search([5], 5) == 0
    assert search([], 1) == -1
