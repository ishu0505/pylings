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
# TODO: write your tests below.

def test_is_even():
    assert is_even(4) == True
    assert is_even(7) == False

def test_neg_even():
    assert is_even(-5) == False
    assert is_even(-2) == True

def test_zero():
    assert is_even(0) == True
