"""
diag5_clamp_tdd — Solution
"""
import pytest


def clamp(val: float, low: float, high: float) -> float:
    if low > high:
        raise ValueError("low cannot be greater than high")
    if val < low:
        return low
    if val > high:
        return high
    return val


# ---------------------------------------------------------------- tests


def test_clamp_in_range():
    assert clamp(5, 0, 10) == 5
    assert clamp(0, 0, 10) == 0
    assert clamp(10, 0, 10) == 10


def test_clamp_out_of_range():
    assert clamp(-5, 0, 10) == 0
    assert clamp(15, 0, 10) == 10


def test_clamp_invalid_bounds():
    with pytest.raises(ValueError):
        clamp(5, 10, 0)
