"""
tdd3_error_testing — Solution
"""
import pytest


def transfer_funds(source: dict, target: dict, amount: float) -> None:
    if amount <= 0:
        raise ValueError("amount must be positive")
    if source["balance"] < amount:
        raise ValueError("insufficient funds")
    source["balance"] -= amount
    target["balance"] += amount


# ---------------------------------------------------------------- tests


def test_transfer_success():
    src = {"balance": 100.0}
    dst = {"balance": 50.0}
    transfer_funds(src, dst, 30.0)
    assert src["balance"] == 70.0
    assert dst["balance"] == 80.0


def test_negative_or_zero_amount():
    src = {"balance": 100.0}
    dst = {"balance": 50.0}
    with pytest.raises(ValueError):
        transfer_funds(src, dst, 0.0)
    with pytest.raises(ValueError):
        transfer_funds(src, dst, -10.0)


def test_insufficient_funds():
    src = {"balance": 20.0}
    dst = {"balance": 50.0}
    with pytest.raises(ValueError):
        transfer_funds(src, dst, 50.0)
