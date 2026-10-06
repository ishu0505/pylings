"""
koko_eating_bananas — Koko Eating Bananas (NeetCode)   difficulty: medium

Koko loves to eat bananas. There are n piles of bananas, the ith pile has piles[i] bananas.
Koko can decide her bananas-per-hour eating speed of k. Each hour, she chooses some pile and eats
k bananas from it. She has h hours to eat all bananas.
Return the minimum integer k such that she can eat all the bananas within h hours.
Goal: O(n * log(max(piles))) time.
"""

# I AM NOT DONE

# Concept Tip: When the search range is answers (1 to max), binary search finds the minimum feasible rate.
import math


def min_eating_speed(piles: list[int], h: int) -> int:
    # TODO: implement
    raise NotImplementedError


# ---------------------------------------------------------------- tests


def test_koko():
    assert min_eating_speed([3, 6, 7, 11], 8) == 4
    assert min_eating_speed([30, 11, 23, 4, 20], 5) == 30
    assert min_eating_speed([30, 11, 23, 4, 20], 6) == 23
