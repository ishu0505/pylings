"""
diag5_clamp_tdd — You write the tests (TDD mode)       difficulty: easy

clamp(val, low, high) constrains `val` such that low <= val <= high.
If low > high, it raises ValueError.

Your task: write tests that thoroughly verify clamp, including edge cases and errors.
At least 3 zero-argument test_* functions.
"""

# I AM NOT DONE

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
