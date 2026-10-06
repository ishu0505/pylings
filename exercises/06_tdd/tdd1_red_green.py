"""
tdd1_red_green — Implement from tests first             difficulty: easy

Implement `calculate_cart_total(items: list[dict], discount_code: str | None = None) -> float`:
- each item is `{"price": float, "quantity": int}`
- computes subtotal
- if discount_code == "SAVE10", applies 10% discount
- if discount_code == "HALF", applies 50% discount
- returns final total rounded to 2 decimal places
- if items is empty, returns 0.0
"""

# I AM NOT DONE

# Concept Tip: In TDD, the test assertions define the functional specification.


def calculate_cart_total(items: list[dict], discount_code: str | None = None) -> float:
    # TODO: implement to satisfy tests below
    raise NotImplementedError


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
