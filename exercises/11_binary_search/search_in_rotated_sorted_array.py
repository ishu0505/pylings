"""
search_in_rotated_sorted_array — Search in Rotated Sorted Array (NeetCode) difficulty: medium

Given array nums sorted in ascending order (with distinct values) and possibly rotated,
return the index of target, or -1 if not in nums.
Goal: O(log n) time.
"""

# I AM NOT DONE

# Concept Tip: If `nums[lo] <= nums[mid]`, the left half is normally sorted. Otherwise, the right half is sorted.


def search_rotated(nums: list[int], target: int) -> int:
    # TODO: implement in O(log n)
    raise NotImplementedError


# ---------------------------------------------------------------- tests


def test_search_rotated():
    assert search_rotated([4, 5, 6, 7, 0, 1, 2], 0) == 4
    assert search_rotated([4, 5, 6, 7, 0, 1, 2], 3) == -1
    assert search_rotated([1], 0) == -1
