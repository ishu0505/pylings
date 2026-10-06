"""
basics1_truthiness — Solution
"""


def is_none(val: object) -> bool:
    return val is None


def is_truthy(val: object) -> bool:
    return bool(val)


def coalesce(*values: object) -> object:
    for v in values:
        if v is not None:
            return v
    return None


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
