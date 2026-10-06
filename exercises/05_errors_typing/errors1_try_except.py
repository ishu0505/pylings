"""
errors1_try_except — Exception Handling & Chaining     difficulty: easy

1. `safe_parse_int(val: str, default: int = 0) -> int`:
   tries to parse val as int; returns default on ValueError or TypeError.

2. `wrap_database_call(fn, *args)`:
   calls fn(*args). If fn raises KeyError, catch it and raise `DatabaseError("Record not found") from err`.
   If fn succeeds, return its result.
"""

# I AM NOT DONE

# Concept Tip: `raise B from A` preserves original traceback in `__cause__`.


class DatabaseError(Exception):
    pass


def safe_parse_int(val: str, default: int = 0) -> int:
    # TODO: implement
    raise NotImplementedError


def wrap_database_call(fn, *args):
    # TODO: implement
    raise NotImplementedError


# ---------------------------------------------------------------- tests
import pytest


def test_safe_parse_int():
    assert safe_parse_int("42") == 42
    assert safe_parse_int("abc", -1) == -1
    assert safe_parse_int(None, 0) == 0  # type: ignore


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
