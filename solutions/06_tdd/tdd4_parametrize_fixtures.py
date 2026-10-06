"""
tdd4_parametrize_fixtures — Solution
"""
import pytest


def is_valid_password(pw: str) -> bool:
    if len(pw) < 8:
        return False
    has_digit = any(c.isdigit() for c in pw)
    has_upper = any(c.isupper() for c in pw)
    has_lower = any(c.islower() for c in pw)
    return has_digit and has_upper and has_lower


# ---------------------------------------------------------------- tests


@pytest.mark.parametrize(
    "password,expected",
    [
        ("Password123", True),
        ("short1A", False),
        ("alllowercase123", False),
        ("ALLUPPERCASE123", False),
        ("NoDigitsHere", False),
        ("", False),
    ],
)
def test_password_validation(password: str, expected: bool):
    assert is_valid_password(password) is expected
