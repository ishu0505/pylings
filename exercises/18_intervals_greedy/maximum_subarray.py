"""
maximum_subarray — Maximum Subarray (NeetCode)         difficulty: medium

Given an integer array nums, find the subarray with the largest sum, and return its sum.
Goal: O(n) time, O(1) space.
"""

# I AM NOT DONE

# Concept Tip: Kadane's algorithm discards negative running prefixes greedily.


def max_sub_array(nums: list[int]) -> int:
    # TODO: implement
    raise NotImplementedError


# ---------------------------------------------------------------- tests


def test_max_sub_array():
    assert max_sub_array([-2, 1, -3, 4, -1, 2, 1, -5, 4]) == 6
    assert max_sub_array([1]) == 1
    assert max_sub_array([5, 4, -1, 7, 8]) == 23
    assert max_sub_array([-1, -2]) == -1
