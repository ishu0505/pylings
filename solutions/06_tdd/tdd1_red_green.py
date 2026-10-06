"""
tdd1_red_green — Solution
"""


def calculate_cart_total(items: list[dict], discount_code: str | None = None) -> float:
    if not items:
        return 0.0
    subtotal = sum(item["price"] * item["quantity"] for item in items)
    if discount_code == "SAVE10":
        subtotal *= 0.90
    elif discount_code == "HALF":
        subtotal *= 0.50
    return round(subtotal, 2)


# ---------------------------------------------------------------- tests


def test_empty_cart():
    assert calculate_cart_total([]) == 0.0


def test_standard_cart_no_discount():
    items = [{"price": 10.0, "quantity": 2}, {"price": 5.0, "quantity": 1}]
    assert calculate_cart_total(items) == 25.0


def test_discounts():
    items = [{"price": 100.0, "quantity": 1}]
    assert calculate_cart_total(items, "SAVE10") == 90.0
    assert calculate_cart_total(items, "HALF") == 50.0
    assert calculate_cart_total(items, "UNKNOWN") == 100.0
