"""
largest_rectangle_in_histogram — Largest Rectangle in Histogram (NeetCode) difficulty: hard

Given an array of integers heights representing the histogram's bar height where
the width of each bar is 1, return the area of the largest rectangle in the histogram.
Goal: O(n) time.
"""

# I AM NOT DONE

# Concept Tip: When a bar is popped, it cannot extend to the right anymore, so its maximum area is finalized.


def largest_rectangle_area(heights: list[int]) -> int:
    # TODO: implement in O(n)
    raise NotImplementedError


# ---------------------------------------------------------------- tests


def test_largest_rectangle():
    assert largest_rectangle_area([2, 1, 5, 6, 2, 3]) == 10
    assert largest_rectangle_area([2, 4]) == 4
    assert largest_rectangle_area([]) == 0
    assert largest_rectangle_area([1]) == 1
