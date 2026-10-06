"""
contains_duplicate — Contains Duplicate (NeetCode)     difficulty: easy

Given an integer array nums, return true if any value appears at least twice in the array,
and return false if every element is distinct.
Goal: O(n) time, O(n) space.
"""

# I AM NOT DONE

# Concept Tip: Set membership check `x in seen` runs in O(1) average time.


def contains_duplicate(nums: list[int]) -> bool:
    # TODO: implement
    raise NotImplementedError


# ---------------------------------------------------------------- tests


def test_contains_duplicate():
    assert contains_duplicate([1, 2, 3, 1]) is True
    assert contains_duplicate([1, 2, 3, 4]) is False
    assert contains_duplicate([1, 1, 1, 3, 3, 4, 3, 2, 4, 2]) is True
    assert contains_duplicate([]) is False
