"""
best_time_to_buy_sell_stock — Solution
"""


def max_profit(prices: list[int]) -> int:
    min_price = float("inf")
    best = 0
    for p in prices:
        if p < min_price:
            min_price = p
        elif p - min_price > best:
            best = p - min_price
    return best


# ---------------------------------------------------------------- tests


def test_max_profit():
    assert max_profit([7, 1, 5, 3, 6, 4]) == 5
    assert max_profit([7, 6, 4, 3, 1]) == 0
    assert max_profit([]) == 0
    assert max_profit([1]) == 0
