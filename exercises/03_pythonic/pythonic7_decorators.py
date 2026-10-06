"""
pythonic7_decorators — Writing decorators               difficulty: hard

Implement:
1. `record_calls(fn)`:
   decorator that tracks how many times `fn` was called via an attribute `fn.call_count`.
   Preserves fn's docstring and name using `@functools.wraps`.

2. `retry(max_attempts: int, delay: float = 0.0)`:
   decorator factory that retries the wrapped function up to max_attempts on any Exception.
   If all attempts fail, raises the final exception.
"""

# I AM NOT DONE

# Concept Tip: Decorators wrap functions with extra behavior (logging, auth, retry) without altering the function's internal logic.
from functools import wraps
from typing import Callable


def record_calls(fn: Callable) -> Callable:
    # TODO: implement
    raise NotImplementedError


def retry(max_attempts: int, delay: float = 0.0) -> Callable:
    # TODO: implement
    raise NotImplementedError


# ---------------------------------------------------------------- tests
import pytest


def test_record_calls():
    @record_calls
    def add(a: int, b: int) -> int:
        """Add two numbers."""
        return a + b

    assert add.__name__ == "add"
    assert add.__doc__ == "Add two numbers."
    assert add.call_count == 0

    assert add(2, 3) == 5
    assert add.call_count == 1
    assert add(10, 20) == 30
    assert add.call_count == 2


def test_retry_success():
    attempts = 0

    @retry(max_attempts=3)
    def flaky():
        nonlocal attempts
        attempts += 1
        if attempts < 2:
            raise ValueError("temporary error")
        return "success"

    assert flaky() == "success"
    assert attempts == 2


def test_retry_exhausted():
    @retry(max_attempts=2)
    def always_fails():
        raise RuntimeError("boom")

    with pytest.raises(RuntimeError) as exc:
        always_fails()
    assert "boom" in str(exc.value)
