"""
tdd3_error_testing — You write the tests (TDD mode)    difficulty: medium

`transfer_funds(source: dict, target: dict, amount: float) -> None`:
- amount must be > 0 (else ValueError("amount must be positive"))
- source["balance"] must be >= amount (else ValueError("insufficient funds"))
- subtracts amount from source["balance"] and adds to target["balance"]

Write at least 3 tests covering success and both error conditions.
"""

# I AM NOT DONE

# Concept Tip: `pytest.raises` checks both that an exception was raised and optionally its message.


def transfer_funds(source: dict, target: dict, amount: float) -> None:
    if amount <= 0:
        raise ValueError("amount must be positive")
    if source["balance"] < amount:
        raise ValueError("insufficient funds")
    source["balance"] -= amount
    target["balance"] += amount


# ---------------------------------------------------------------- tests
# TODO: write your tests below.
