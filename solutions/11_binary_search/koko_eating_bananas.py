"""
koko_eating_bananas — Solution
"""
import math


def min_eating_speed(piles: list[int], h: int) -> int:
    lo, hi = 1, max(piles)
    res = hi

    while lo <= hi:
        k = (lo + hi) // 2
        hours = sum(math.ceil(p / k) for p in piles)
        if hours <= h:
            res = k
            hi = k - 1
        else:
            lo = k + 1
    return res


# ---------------------------------------------------------------- tests


def test_koko():
    assert min_eating_speed([3, 6, 7, 11], 8) == 4
    assert min_eating_speed([30, 11, 23, 4, 20], 5) == 30
    assert min_eating_speed([30, 11, 23, 4, 20], 6) == 23
