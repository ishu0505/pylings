"""
errors6_result_type — Solution
"""
from typing import Any, Callable


class Ok:
    def __init__(self, value: Any) -> None:
        self.value = value

    def is_ok(self) -> bool:
        return True

    def is_err(self) -> bool:
        return False

    def unwrap(self) -> Any:
        return self.value

    def unwrap_or(self, default: Any) -> Any:
        return self.value

    def map(self, fn: Callable[[Any], Any]) -> "Ok":
        return Ok(fn(self.value))


class Err:
    def __init__(self, error: Any) -> None:
        self.error = error

    def is_ok(self) -> bool:
        return False

    def is_err(self) -> bool:
        return True

    def unwrap(self) -> Any:
        raise RuntimeError(str(self.error))

    def unwrap_or(self, default: Any) -> Any:
        return default

    def map(self, fn: Callable[[Any], Any]) -> "Err":
        return self


# ---------------------------------------------------------------- tests
import pytest


def test_ok():
    res = Ok(10)
    assert res.is_ok() is True
    assert res.is_err() is False
    assert res.unwrap() == 10
    assert res.unwrap_or(0) == 10

    mapped = res.map(lambda x: x * 2)
    assert mapped.is_ok()
    assert mapped.unwrap() == 20


def test_err():
    res = Err("database timeout")
    assert res.is_ok() is False
    assert res.is_err() is True
    assert res.unwrap_or(0) == 0

    with pytest.raises(RuntimeError) as exc:
        res.unwrap()
    assert "database timeout" in str(exc.value)

    mapped = res.map(lambda x: x * 2)
    assert mapped.is_err()
    assert mapped.unwrap_or(0) == 0
