"""
errors1_try_except — Solution
"""


class DatabaseError(Exception):
    pass


def safe_parse_int(val: str, default: int = 0) -> int:
    try:
        return int(val)
    except (ValueError, TypeError):
        return default


def wrap_database_call(fn, *args):
    try:
        return fn(*args)
    except KeyError as err:
        raise DatabaseError("Record not found") from err


# ---------------------------------------------------------------- tests
import pytest


def test_safe_parse_int():
    assert safe_parse_int("42") == 42
    assert safe_parse_int("abc", -1) == -1
    assert safe_parse_int(None, 0) == 0


def test_wrap_database_call_success():
    def get_user(uid):
        return {"id": uid, "name": "Ada"}

    assert wrap_database_call(get_user, "u1") == {"id": "u1", "name": "Ada"}


def test_wrap_database_call_error_chain():
    def missing(uid):
        raise KeyError(uid)

    with pytest.raises(DatabaseError) as exc_info:
        wrap_database_call(missing, "missing_id")
    assert "Record not found" in str(exc_info.value)
    assert isinstance(exc_info.value.__cause__, KeyError)
