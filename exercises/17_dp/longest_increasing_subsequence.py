"""
longest_increasing_subsequence — LIS (NeetCode)         difficulty: medium

Given an integer array nums, return the length of the longest strictly increasing subsequence.
Goal: O(n log n) or O(n^2) time.
"""

# I AM NOT DONE

# Concept Tip: A subsequence does not have to be contiguous, only maintaining relative order.
import bisect


def length_of_lis(nums: list[int]) -> int:
    # TODO: implement
    raise NotImplementedError


# ---------------------------------------------------------------- tests


def test_lis():
    assert length_of_lis([10, 9, 2, 5, 3, 7, 101, 18]) == 4
    assert length_of_lis([0, 1, 0, 3, 2, 3]) == 4
    assert length_of_lis([7, 7, 7, 7, 7]) == 1
    assert length_of_lis([]) == 0
