"""
errors4_type_hints — Modern typing in Python 3.12     difficulty: medium

1. `class LLMConfig(TypedDict)`:
   fields: `model: str`, `temperature: float`, `max_tokens: int`

2. `first_or_default(items: list[T], default: T) -> T`:
   generic function that returns items[0] if items has elements, else default.
"""

# I AM NOT DONE

# Concept Tip: `TypedDict` gives dictionary objects static type checking without runtime overhead.
from typing import TypeVar, TypedDict

T = TypeVar("T")

# TODO: define LLMConfig and first_or_default


# ---------------------------------------------------------------- tests


def test_typed_dict():
    config: LLMConfig = {"model": "claude-3-5", "temperature": 0.7, "max_tokens": 1024}
    assert config["model"] == "claude-3-5"
    assert config["temperature"] == 0.7


def test_first_or_default():
    assert first_or_default([1, 2, 3], 0) == 1
    assert first_or_default([], 99) == 99
    assert first_or_default(["a", "b"], "default") == "a"
    assert first_or_default([], "fallback") == "fallback"
