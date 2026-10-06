"""
product_except_self — Product of Array Except Self (NeetCode) difficulty: medium

Given an integer array nums, return an array answer such that answer[i] is equal
to the product of all elements of nums except nums[i].
Must run in O(n) time WITHOUT using division.
"""

# I AM NOT DONE

# Concept Tip: `ans[i] = (product of elements before i) * (product of elements after i)`.


def product_except_self(nums: list[int]) -> list[int]:
    # TODO: implement in O(n) without division
    raise NotImplementedError


# ---------------------------------------------------------------- tests


def test_product_except_self():
    assert product_except_self([1, 2, 3, 4]) == [24, 12, 8, 6]
    assert product_except_self([-1, 1, 0, -3, 3]) == [0, 0, 9, 0, 0]
