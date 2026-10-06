"""
oop1_classes_instances — Solution
"""


class BankAccount:
    interest_rate: float = 0.02

    def __init__(self, owner: str, balance: float = 0.0) -> None:
        if balance < 0:
            raise ValueError("initial balance cannot be negative")
        self.owner = owner
        self.balance = balance

    def deposit(self, amount: float) -> None:
        if amount <= 0:
            raise ValueError("deposit must be positive")
        self.balance += amount

    def withdraw(self, amount: float) -> None:
        if amount <= 0:
            raise ValueError("withdraw must be positive")
        if amount > self.balance:
            raise ValueError("insufficient funds")
        self.balance -= amount

    def apply_interest(self) -> None:
        self.balance += self.balance * self.interest_rate


# ---------------------------------------------------------------- tests
import pytest


def test_bank_account_lifecycle():
    acc = BankAccount("Alice", 100.0)
    assert acc.owner == "Alice"
    assert acc.balance == 100.0

    acc.deposit(50.0)
    assert acc.balance == 150.0

    acc.withdraw(30.0)
    assert acc.balance == 120.0

    acc.apply_interest()
    assert acc.balance == 120.0 + (120.0 * 0.02)


def test_bank_account_errors():
    with pytest.raises(ValueError):
        BankAccount("Bob", -10.0)

    acc = BankAccount("Bob", 50.0)
    with pytest.raises(ValueError):
        acc.deposit(0)
    with pytest.raises(ValueError):
        acc.withdraw(100.0)
