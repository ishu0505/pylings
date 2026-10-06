"""
pythonic7_decorators — Solution
"""
from functools import wraps
from typing import Callable


def record_calls(fn: Callable) -> Callable:
    @wraps(fn)
    def wrapper(*args, **kwargs):
        wrapper.call_count += 1
        return fn(*args, **kwargs)

    wrapper.call_count = 0
    return wrapper


def retry(max_attempts: int, delay: float = 0.0) -> Callable:
    def decorator(fn: Callable) -> Callable:
        @wraps(fn)
        def wrapper(*args, **kwargs):
            last_err = None
            for _ in range(max_attempts):
                try:
                    return fn(*args, **kwargs)
                except Exception as err:
                    last_err = err
            if last_err is not None:
                raise last_err
        return wrapper
    return decorator


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
