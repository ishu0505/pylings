"""
diag6_validate_user — Solution
"""


class ValidationError(Exception):
    def __init__(self, errors: dict[str, str]) -> None:
        super().__init__(f"Validation failed: {errors}")
        self.errors = errors


def validate_user_payload(data: dict) -> None:
    errors: dict[str, str] = {}

    username = data.get("username")
    if not isinstance(username, str) or not (3 <= len(username) <= 20):
        errors["username"] = "must be string between 3 and 20 chars"

    age = data.get("age")
    if not isinstance(age, int) or age < 18:
        errors["age"] = "must be an integer >= 18"

    email = data.get("email")
    if not isinstance(email, str) or "@" not in email:
        errors["email"] = "must be string containing '@'"

    if errors:
        raise ValidationError(errors)


# ---------------------------------------------------------------- tests
import pytest


def test_validate_valid():
    payload = {"username": "alice", "age": 25, "email": "alice@example.com"}
    validate_user_payload(payload)


def test_validate_multiple_errors():
    payload = {"username": "a", "age": 16, "email": "invalid_email"}
    with pytest.raises(ValidationError) as exc_info:
        validate_user_payload(payload)
    errs = exc_info.value.errors
    assert "username" in errs
    assert "age" in errs
    assert "email" in errs


def test_validate_missing_fields():
    with pytest.raises(ValidationError) as exc_info:
        validate_user_payload({})
    assert len(exc_info.value.errors) == 3
