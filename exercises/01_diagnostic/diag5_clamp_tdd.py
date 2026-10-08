"""
diag5_clamp_tdd — You write the tests (TDD mode)       difficulty: easy

clamp(val, low, high) constrains `val` such that low <= val <= high.
If low > high, it raises ValueError.

Your task: write tests that thoroughly verify clamp, including edge cases and errors.
At least 3 zero-argument test_* functions.
"""
import pytest

# Concept Tip: Good tests verify: middle values, boundaries (val == low, val == high),
# values outside both ends, and error paths (low > high).


def clamp(val: float, low: float, high: float) -> float:
    if low > high:
        raise ValueError("low cannot be greater than high")
    if val < low:
        return low
    if val > high:
        return high
    return val


# ---------------------------------------------------------------- tests
# TODO: write your tests below.

def test_clamp_inside_and_at_boundaries():
    # A value already inside the range stays the same.
    assert clamp(3, 1, 5) == 3

    # Values exactly at the limits stay at those limits.
    assert clamp(1, 1, 5) == 1
    assert clamp(5, 1, 5) == 5


def test_clamp_outside_range():
    # Too low gets raised to the low limit.
    assert clamp(-2, 1, 5) == 1

    # Too high gets lowered to the high limit.
    assert clamp(8, 1, 5) == 5


def test_low_greater_than_high_raises_error():
    # This input is invalid, so clamp should raise ValueError.
    with pytest.raises(ValueError):
        clamp(3, 5, 1)