"""
best_time_to_buy_sell_stock — Best Time to Buy/Sell Stock (NeetCode) difficulty: easy

You want to maximize your profit by choosing a single day to buy one stock and
choosing a different day in the future to sell that stock. Return the maximum profit.
Goal: O(n) time, O(1) space.
"""

# I AM NOT DONE

# Concept Tip: You only need to remember the historical lowest price before the current day.


def max_profit(prices: list[int]) -> int:
    # TODO: implement in O(n)
    raise NotImplementedError


# ---------------------------------------------------------------- tests


def test_max_profit():
    assert max_profit([7, 1, 5, 3, 6, 4]) == 5
    assert max_profit([7, 6, 4, 3, 1]) == 0
    assert max_profit([]) == 0
    assert max_profit([1]) == 0
