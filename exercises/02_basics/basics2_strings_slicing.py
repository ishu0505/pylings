"""
basics2_strings_slicing — Slicing and f-strings        difficulty: easy

Implement:
1. `reverse_string(s: str) -> str`: reverses the string using slicing.
2. `format_currency(amount: float, symbol: str = "$") -> str`: returns e.g. "$12.50" formatted to 2 decimals.
3. `middle_chars(s: str, n: int) -> str`: returns the middle n characters (assume len(s) >= n and (len(s) - n) is even).
"""

# I AM NOT DONE

# Concept Tip: `s[start:stop:step]` lets you slice strings efficiently in C-speed.


def reverse_string(s: str) -> str:
    # TODO: implement
    raise NotImplementedError


def format_currency(amount: float, symbol: str = "$") -> str:
    # TODO: implement
    raise NotImplementedError


def middle_chars(s: str, n: int) -> str:
    # TODO: implement
    raise NotImplementedError


# ---------------------------------------------------------------- tests


def test_reverse():
    assert reverse_string("python") == "nohtyp"
    assert reverse_string("") == ""


def test_format_currency():
    assert format_currency(12.5) == "$12.50"
    assert format_currency(0.123, "€") == "€0.12"
    assert format_currency(100.0, "¥") == "¥100.00"


def test_middle_chars():
    assert middle_chars("abcdef", 2) == "cd"
    assert middle_chars("racecar", 3) == "cec"
