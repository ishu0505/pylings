"""
tdd4_parametrize_fixtures — Parametrized Tests         difficulty: medium

Implement `is_valid_password(pw: str) -> bool`:
- at least 8 characters
- contains at least one digit
- contains at least one uppercase letter
- contains at least one lowercase letter
"""

# I AM NOT DONE

# Concept Tip: `@pytest.mark.parametrize` runs the same test body across a table of cases.


def is_valid_password(pw: str) -> bool:
    # TODO: implement
    raise NotImplementedError


# ---------------------------------------------------------------- tests
import pytest


@pytest.mark.parametrize(
    "password,expected",
    [
        ("Password123", True),
        ("short1A", False),          # < 8 chars
        ("alllowercase123", False),  # no uppercase
        ("ALLUPPERCASE123", False),  # no lowercase
        ("NoDigitsHere", False),     # no digit
        ("", False),
    ],
)
def test_password_validation(password: str, expected: bool):
    assert is_valid_password(password) is expected
