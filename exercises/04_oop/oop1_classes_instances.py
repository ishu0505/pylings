"""
oop1_classes_instances — BankAccount class             difficulty: easy

Build `BankAccount`:
- class attribute `interest_rate: float = 0.02`
- `__init__(self, owner: str, balance: float = 0.0)`: raises ValueError if initial balance < 0
- `deposit(self, amount: float) -> None`: adds to balance (raises ValueError if amount <= 0)
- `withdraw(self, amount: float) -> None`: subtracts from balance (raises ValueError if amount <= 0 or amount > balance)
- `apply_interest(self) -> None`: adds balance * interest_rate to balance
"""

# I AM NOT DONE

# Concept Tip: `self` is an explicit reference to the specific instance calling the method.


class BankAccount:
    # TODO: implement
    pass


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
