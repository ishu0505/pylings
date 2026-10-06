"""
two_sum_ii — Two Sum II - Input Array Is Sorted (NeetCode) difficulty: medium

Given a 1-indexed array of integers numbers that is already sorted in non-decreasing order,
find two numbers such that they add up to target. Return their indices [index1, index2] (1-indexed).
Goal: O(n) time, O(1) space.
"""

# I AM NOT DONE

# Concept Tip: When numbers are sorted, moving `l` right increases the sum and moving `r` left decreases it.


def two_sum_sorted(numbers: list[int], target: int) -> list[int]:
    # TODO: implement in O(n) time, O(1) space
    raise NotImplementedError


# ---------------------------------------------------------------- tests


def test_two_sum_sorted():
    assert two_sum_sorted([2, 7, 11, 15], 9) == [1, 2]
    assert two_sum_sorted([2, 3, 4], 6) == [1, 3]
    assert two_sum_sorted([-1, 0], -1) == [1, 2]
