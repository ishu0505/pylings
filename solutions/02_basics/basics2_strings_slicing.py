"""
basics2_strings_slicing — Solution
"""


def reverse_string(s: str) -> str:
    return s[::-1]


def format_currency(amount: float, symbol: str = "$") -> str:
    return f"{symbol}{amount:.2f}"


def middle_chars(s: str, n: int) -> str:
    start = (len(s) - n) // 2
    return s[start:start + n]


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
