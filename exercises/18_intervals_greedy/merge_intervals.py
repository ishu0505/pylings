"""
merge_intervals — Merge Intervals (NeetCode)           difficulty: medium

Given an array of intervals where intervals[i] = [start_i, end_i], merge all overlapping intervals.
Goal: O(n log n) time.
"""

# I AM NOT DONE

# Concept Tip: Sorting by start time ensures overlapping intervals are always adjacent in the list.


def merge(intervals: list[list[int]]) -> list[list[int]]:
    # TODO: implement
    raise NotImplementedError


# ---------------------------------------------------------------- tests


def test_merge_intervals():
    assert merge([[1, 3], [2, 6], [8, 10], [15, 18]]) == [[1, 6], [8, 10], [15, 18]]
    assert merge([[1, 4], [4, 5]]) == [[1, 5]]
    assert merge([]) == []
