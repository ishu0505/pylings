"""
errors6_result_type — Result[T, E] Container (Rust bridge)   difficulty: hard

Implement `Result[T, E]`:
- `Ok(value)`: represents success
- `Err(error)`: represents failure
- Methods on both:
  - `is_ok() -> bool`
  - `is_err() -> bool`
  - `unwrap() -> T`: returns value on Ok; raises RuntimeError(error) on Err
  - `unwrap_or(default: T) -> T`: returns value on Ok, default on Err
  - `map(fn: Callable[[T], U]) -> Result[U, E]`: applies fn to value on Ok, returns Err untouched
"""

# I AM NOT DONE

# Concept Tip: Result types eliminate unhandled runtime exceptions by making errors part of the return type.
from typing import Any, Callable


class Ok:
    # TODO: implement
    pass


class Err:
    # TODO: implement
    pass


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
