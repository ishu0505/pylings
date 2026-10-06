"""
errors5_pydantic — Solution
"""
from pydantic import BaseModel, Field, field_validator


class UserRegistration(BaseModel):
    username: str = Field(min_length=3, max_length=20)
    email: str
    age: int = Field(ge=18)
    tags: list[str] = Field(default_factory=list)

    @field_validator("email")
    @classmethod
    def validate_email(cls, v: str) -> str:
        if "@" not in v or "." not in v:
            raise ValueError("invalid email format")
        return v


# ---------------------------------------------------------------- tests
import pytest
from pydantic import ValidationError


def test_valid_user():
    u = UserRegistration(username="alice", email="alice@test.com", age=25)
    assert u.username == "alice"
    assert u.email == "alice@test.com"
    assert u.age == 25
    assert u.tags == []
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
