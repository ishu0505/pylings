"""
car_fleet — Car Fleet (NeetCode)                       difficulty: medium

There are n cars at given miles along a one-lane road heading towards target miles.
A car can never pass another car ahead of it, but it can catch up to it and form a fleet.
Return the number of car fleets that will arrive at the destination.
Goal: O(n log n) time.
"""

# I AM NOT DONE

# Concept Tip: Cars ahead set the pace. A faster trailing car gets trapped behind the fleet in front of it.


def car_fleet(target: int, position: list[int], speed: list[int]) -> int:
    # TODO: implement
    raise NotImplementedError


# ---------------------------------------------------------------- tests


def test_car_fleet():
    assert car_fleet(12, [10, 8, 0, 5, 3], [2, 4, 1, 1, 3]) == 3
    assert car_fleet(10, [3], [3]) == 1
    assert car_fleet(100, [0, 2, 4], [4, 2, 1]) == 1
