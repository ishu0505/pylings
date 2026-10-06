"""
climbing_stairs — Solution
"""


def climb_stairs(n: int) -> int:
    if n <= 2:
        return n
    one, two = 1, 2
    for _ in range(3, n + 1):
        one, two = two, one + two
    return two


# ---------------------------------------------------------------- tests


def test_climb_stairs():
    assert climb_stairs(2) == 2
    assert climb_stairs(3) == 3
    assert climb_stairs(5) == 8
    assert climb_stairs(1) == 1
