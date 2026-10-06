"""
daily_temperatures — Daily Temperatures (NeetCode)     difficulty: medium

Given an array of integers temperatures, return an array answer such that answer[i]
is the number of days you have to wait after the ith day to get a warmer temperature.
If there is no future day for which this is possible, keep answer[i] == 0.
Goal: O(n) time.
"""

# I AM NOT DONE

# Concept Tip: A monotonic decreasing stack resolves the 'next greater element' for all waiting days in O(1) amortized time.


def daily_temperatures(temperatures: list[int]) -> list[int]:
    # TODO: implement in O(n)
    raise NotImplementedError


# ---------------------------------------------------------------- tests


def test_daily_temperatures():
    assert daily_temperatures([73, 74, 75, 71, 69, 72, 76, 73]) == [1, 1, 4, 2, 1, 1, 0, 0]
    assert daily_temperatures([30, 40, 50, 60]) == [1, 1, 1, 0]
    assert daily_temperatures([30, 60, 90]) == [1, 1, 0]
