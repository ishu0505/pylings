"""
intro2 — Fix a failing function                           difficulty: easy

The test below is RED. Read pytest's output: it shows what `greet` returned
and what the test expected. Fix `greet` so it goes GREEN.

Run:  uv run pylings run intro2      Hint: uv run pylings hint intro2
"""


# Concept Tip: f-strings embed expressions: f"{x} + {y} = {x + y}"


def greet(name: str) -> str:
    # TODO: fix the bug
    name = name.strip()
    return f"Hello, {name}!"


# ---------------------------------------------------------------- tests


def test_greet():
    assert greet("Ada") == "Hello, Ada!"


def test_greet_strips_whitespace():
    assert greet("  Linus ") == "Hello, Linus!"
