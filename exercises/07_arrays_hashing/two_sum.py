"""
two_sum — Two Sum (NeetCode)                           difficulty: easy

Given an array of integers nums and an integer target, return indices of the two
numbers such that they add up to target. Exactly one solution exists.
Goal: O(n) time.
"""

# I AM NOT DONE

# Concept Tip: As you iterate, check if `target - num` was already seen before adding `num` to the map.


def two_sum(nums: list[int], target: int) -> list[int]:
    # TODO: implement in O(n)
    raise NotImplementedError


# ---------------------------------------------------------------- tests


def test_two_sum():
    assert two_sum([2, 7, 11, 15], 9) == [0, 1]
    assert two_sum([3, 2, 4], 6) == [1, 2]
    assert two_sum([3, 3], 6) == [0, 1]
