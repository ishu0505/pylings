"""
coin_change — Coin Change (NeetCode)                   difficulty: medium

Given an integer array coins and an integer amount, return the fewest number of coins
that you need to make up that amount. If that amount cannot be made up, return -1.
Goal: O(amount * len(coins)) time.
"""

# I AM NOT DONE

# Concept Tip: Building amounts bottom-up from 1 to amount guarantees optimal subproblems.


def coin_change(coins: list[int], amount: int) -> int:
    # TODO: implement
    raise NotImplementedError


# ---------------------------------------------------------------- tests


def test_coin_change():
    assert coin_change([1, 2, 5], 11) == 3
    assert coin_change([2], 3) == -1
    assert coin_change([1], 0) == 0
