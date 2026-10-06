"""
errors5_pydantic — Pydantic v2 Models                   difficulty: medium

Build `UserRegistration`:
- `username: str` with `Field(min_length=3, max_length=20)`
- `email: str`
- `age: int` with `Field(ge=18)`
- `tags: list[str] = Field(default_factory=list)`
- field validator on `email`: checks that it contains "@" and ".", else raises ValueError("invalid email format")
"""

# I AM NOT DONE

# Concept Tip: Pydantic v2 is the backbone of FastAPI data validation.
from pydantic import BaseModel, Field, field_validator


# TODO: implement UserRegistration


# ---------------------------------------------------------------- tests
import pytest
from pydantic import ValidationError


def test_valid_user():
    u = UserRegistration(username="alice", email="alice@test.com", age=25)
    assert u.username == "alice"
    assert u.email == "alice@test.com"
    assert u.age == 25
    assert u.tags == []
    # Test JSON dump
    data = u.model_dump()
    assert data["username"] == "alice"


def test_invalid_age_and_username():
    with pytest.raises(ValidationError):
        UserRegistration(username="al", email="valid@test.com", age=25)

    with pytest.raises(ValidationError):
        UserRegistration(username="alice", email="valid@test.com", age=16)


def test_invalid_email():
    with pytest.raises(ValidationError) as exc:
        UserRegistration(username="alice", email="bad_email", age=25)
    assert "invalid email format" in str(exc.value)
