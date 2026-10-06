"""
trapping_rain_water — Trapping Rain Water (NeetCode)    difficulty: hard

Given n non-negative integers representing an elevation map where width of each bar is 1,
compute how much water it can trap after raining.
Goal: O(n) time, O(1) auxiliary space.
"""

# I AM NOT DONE

# Concept Tip: Whichever side has the smaller boundary limits the water height at that position.


def trap(height: list[int]) -> int:
    # TODO: implement in O(n) time and O(1) space
    raise NotImplementedError


# ---------------------------------------------------------------- tests


def test_trap_water():
    assert trap([0, 1, 0, 2, 1, 0, 1, 3, 2, 1, 2, 1]) == 6
    assert trap([4, 2, 0, 3, 2, 5]) == 9
    assert trap([]) == 0
    assert trap([1, 2]) == 0
