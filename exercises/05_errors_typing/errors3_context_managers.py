"""
errors3_context_managers — Custom Context Managers    difficulty: medium

1. `SuppressErrors(*exc_classes)`:
   a class-based context manager that catches and suppresses any exceptions
   of type exc_classes, but lets any other exception propagate.

2. `@contextmanager def temp_override(d: dict, key: str, temp_value: any)`:
   temporarily sets `d[key] = temp_value` inside the context block,
   and restores the original value (or deletes the key if it didn't exist) when exiting,
   even if an exception occurs inside the block.
"""

# I AM NOT DONE

# Concept Tip: `__exit__` guarantees cleanup runs via the language's unwind mechanism.
from contextlib import contextmanager
from typing import Any, Iterator


class SuppressErrors:
    # TODO: implement
    pass


@contextmanager
def temp_override(d: dict[str, Any], key: str, temp_value: Any) -> Iterator[None]:
    # TODO: implement
    raise NotImplementedError


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
