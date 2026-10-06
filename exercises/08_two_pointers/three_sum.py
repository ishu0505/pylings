"""
three_sum — 3Sum (NeetCode)                            difficulty: medium

Given an integer array nums, return all triplets [nums[i], nums[j], nums[k]]
such that i != j, i != k, and j != k, and nums[i] + nums[j] + nums[k] == 0.
The solution set must not contain duplicate triplets.
Goal: O(n^2) time.
"""

# I AM NOT DONE

# Concept Tip: Sorting first allows duplicate skipping with a simple pointer check.


def three_sum(nums: list[int]) -> list[list[int]]:
    # TODO: implement in O(n^2)
    raise NotImplementedError


# ---------------------------------------------------------------- tests


def test_three_sum():
    res = three_sum([-1, 0, 1, 2, -1, -4])
    sorted_res = sorted([sorted(t) for t in res])
    assert sorted_res == [[-1, -1, 2], [-1, 0, 1]]
    assert three_sum([0, 1, 1]) == []
    assert three_sum([0, 0, 0]) == [[0, 0, 0]]
