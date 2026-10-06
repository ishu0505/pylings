"""
container_with_most_water — Container With Most Water (NeetCode) difficulty: medium

Given an integer array height of length n, find two lines that together with the
x-axis form a container that contains the most water. Return the maximum amount of water.
Goal: O(n) time, O(1) space.
"""

# I AM NOT DONE

# Concept Tip: The width `(r - l)` shrinks at each step, so the only hope for a larger area is finding a taller bar.


def max_area(height: list[int]) -> int:
    # TODO: implement in O(n)
    raise NotImplementedError


# ---------------------------------------------------------------- tests


def test_max_area():
    assert max_area([1, 8, 6, 2, 5, 4, 8, 3, 7]) == 49
    assert max_area([1, 1]) == 1
    assert max_area([4, 3, 2, 1, 4]) == 16
