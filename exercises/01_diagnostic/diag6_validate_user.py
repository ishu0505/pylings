"""
diag6_validate_user — Custom ValidationError        difficulty: easy

Create a ValidationError(Exception) class that holds an `errors: dict[str, str]`.
Write `validate_user_payload(data: dict) -> None`:
- "username": must be present, must be str, must be between 3 and 20 chars long.
- "age": must be present, int, >= 18.
- "email": must be present, str, must contain "@".

If one or more fields are invalid, raise ValidationError with a dict mapping
field name -> error description. If all valid, return None.
"""

# I AM NOT DONE

# Concept Tip: Aggregate errors rather than failing on the first one so the caller
# sees everything wrong in one pass.


class ValidationError(Exception):
    # TODO: implement
    pass


def validate_user_payload(data: dict) -> None:
    # TODO: implement
    raise NotImplementedError


# ---------------------------------------------------------------- tests
import pytest


def test_validate_valid():
    payload = {"username": "alice", "age": 25, "email": "alice@example.com"}
    validate_user_payload(payload)  # should not raise


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
