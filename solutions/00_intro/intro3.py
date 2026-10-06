"""
intro3 — You write the tests (TDD mode)                   difficulty: easy

In TDD-mode exercises the implementation is already correct. YOUR job is to
write tests. pylings then plants realistic bugs ("mutants") into `is_even`
and re-runs your tests. Every bug must make at least one test fail.

Rules: at least 2 test functions, named test_*, taking no arguments.

Run:  uv run pylings run intro3      Hint: uv run pylings hint intro3
"""


# Concept Tip: a good test suite checks normal cases AND boundaries (0, negatives).


def is_even(n: int) -> bool:
    return n % 2 == 0


# ---------------------------------------------------------------- tests


def test_positive_numbers():
    assert is_even(4) is True
    assert is_even(7) is False


def test_zero_is_even():
    assert is_even(0) is True


def test_negative_numbers():
    assert is_even(-4) is True
    assert is_even(-3) is False
