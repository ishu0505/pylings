"""
errors3_context_managers — Solution
"""
from contextlib import contextmanager
from typing import Any, Iterator


class SuppressErrors:
    def __init__(self, *exceptions: type[BaseException]) -> None:
        self.exceptions = exceptions

    def __enter__(self) -> "SuppressErrors":
        return self

    def __exit__(self, exc_type: Any, exc_val: Any, exc_tb: Any) -> bool:
        if exc_type is not None and issubclass(exc_type, self.exceptions):
            return True
        return False


@contextmanager
def temp_override(d: dict[str, Any], key: str, temp_value: Any) -> Iterator[None]:
    has_key = key in d
    old_value = d.get(key)
    d[key] = temp_value
    try:
        yield
    finally:
        if has_key:
            d[key] = old_value
        else:
            d.pop(key, None)


# ---------------------------------------------------------------- tests
import pytest


def test_suppress_errors():
    with SuppressErrors(KeyError, ValueError):
        raise KeyError("suppressed")

    with pytest.raises(ZeroDivisionError):
        with SuppressErrors(KeyError):
            _ = 1 / 0


def test_temp_override_existing():
    config = {"env": "prod"}
    with temp_override(config, "env", "test"):
        assert config["env"] == "test"
    assert config["env"] == "prod"


def test_temp_override_new_key_and_exception():
    config = {"env": "prod"}
    with pytest.raises(RuntimeError):
        with temp_override(config, "debug", True):
            assert config["debug"] is True
            raise RuntimeError("fail")
    assert "debug" not in config
