"""
errors4_type_hints — Solution
"""
from typing import TypeVar, TypedDict

T = TypeVar("T")


class LLMConfig(TypedDict):
    model: str
    temperature: float
    max_tokens: int


def first_or_default(items: list[T], default: T) -> T:
    if items:
        return items[0]
    return default


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
