"""
oop3_properties — Solution
"""


class Product:
    def __init__(self, name: str, price: float) -> None:
        self.name = name
        self.price = price
        self.discount_rate = 0.0

    @property
    def price(self) -> float:
        return self._price

    @price.setter
    def price(self, value: float) -> None:
        if value <= 0:
            raise ValueError("price must be positive")
        self._price = float(value)

    @property
    def discount_rate(self) -> float:
        return self._discount_rate

    @discount_rate.setter
    def discount_rate(self, value: float) -> None:
        if not (0.0 <= value <= 1.0):
            raise ValueError("discount rate must be between 0.0 and 1.0")
        self._discount_rate = float(value)

    @property
    def final_price(self) -> float:
        return self._price * (1.0 - self._discount_rate)


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
