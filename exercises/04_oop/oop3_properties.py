"""
oop3_properties — Properties with Encapsulation & Validation   difficulty: easy

Build `Product`:
- `__init__(self, name: str, price: float)`
- property `price`: must be positive (float > 0), else raises ValueError.
- property `discount_rate`: float between 0.0 and 1.0 (defaults to 0.0). Raises ValueError if < 0 or > 1.
- read-only property `final_price`: returns `price * (1 - discount_rate)`.
"""

# I AM NOT DONE

# Concept Tip: Properties give getters/setters without breaking public attribute syntax (`obj.price = 10`).


class Product:
    # TODO: implement
    pass


# ---------------------------------------------------------------- tests
import pytest


def test_product_properties():
    p = Product("Keyboard", 100.0)
    assert p.price == 100.0
    assert p.discount_rate == 0.0
    assert p.final_price == 100.0

    p.discount_rate = 0.20
    assert p.final_price == 80.0

    p.price = 200.0
    assert p.final_price == 160.0


def test_product_validation():
    with pytest.raises(ValueError):
        Product("Mouse", -10.0)

    p = Product("Monitor", 150.0)
    with pytest.raises(ValueError):
        p.price = 0.0
    with pytest.raises(ValueError):
        p.discount_rate = 1.5
