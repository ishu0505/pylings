"""
basics1_truthiness — Truthiness & Identity Checks       difficulty: easy

Implement:
1. `is_none(val)`: returns True if val is None, False otherwise.
2. `is_truthy(val)`: returns True if val is truthy, False if falsy.
3. `coalesce(*values)`: returns the first non-None value, or None if all are None.
"""

# I AM NOT DONE

# Concept Tip: `x is None` checks object identity. `bool(x)` checks truthiness.


def is_none(val: object) -> bool:
    # TODO: implement
    raise NotImplementedError


def is_truthy(val: object) -> bool:
    # TODO: implement
    raise NotImplementedError


def coalesce(*values: object) -> object:
    # TODO: implement
    raise NotImplementedError


# ---------------------------------------------------------------- tests


def test_is_none():
    assert is_none(None) is True
    assert is_none(False) is False
    assert is_none(0) is False
    assert is_none("") is False


def test_is_truthy():
    assert is_truthy(True) is True
    assert is_truthy("hello") is True
    assert is_truthy([1]) is True
    assert is_truthy(False) is False
    assert is_truthy(0) is False
    assert is_truthy("") is False
    assert is_truthy([]) is False


def test_coalesce():
    assert coalesce(None, None, "found", "ignored") == "found"
    assert coalesce(None, False, True) is False
    assert coalesce(None, None) is None
    assert coalesce(0, None) == 0
