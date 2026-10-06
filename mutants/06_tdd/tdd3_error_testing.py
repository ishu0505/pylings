TARGET = "transfer_funds"


def _allows_negative(source, target, amount):
    if source["balance"] < amount:
        raise ValueError("insufficient funds")
    source["balance"] -= amount
    target["balance"] += amount


def _allows_overdraft(source, target, amount):
    if amount <= 0:
        raise ValueError("amount must be positive")
    source["balance"] -= amount
    target["balance"] += amount


def _corrupts_target_balance(source, target, amount):
    if amount <= 0:
        raise ValueError("amount must be positive")
    if source["balance"] < amount:
        raise ValueError("insufficient funds")
    source["balance"] -= amount


MUTANTS = {
    "allows negative or zero transfer amount": _allows_negative,
    "allows overdraft without raising ValueError": _allows_overdraft,
    "does not credit the target balance": _corrupts_target_balance,
}
