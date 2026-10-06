"""
climbing_stairs — Climbing Stairs (NeetCode)           difficulty: easy

You are climbing a staircase. It takes n steps to reach the top.
Each time you can either climb 1 or 2 steps. In how many distinct ways can you climb to the top?
Goal: O(n) time, O(1) space.
"""

# I AM NOT DONE

# Concept Tip: To reach step n, you must take 1 step from (n-1) or 2 steps from (n-2).


def climb_stairs(n: int) -> int:
    # TODO: implement
    raise NotImplementedError


# ---------------------------------------------------------------- tests


def test_climb_stairs():
    assert climb_stairs(2) == 2
    assert climb_stairs(3) == 3
    assert climb_stairs(5) == 8
    assert climb_stairs(1) == 1
