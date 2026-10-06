"""
oop4_class_static_methods — Class methods and factories   difficulty: easy

Build `User`:
- `__init__(self, username: str, email: str, role: str = "member")`
- classmethod `from_csv_line(cls, line: str) -> User`: parses `"alice,alice@example.com,admin"`
- classmethod `from_dict(cls, data: dict) -> User`: parses `{"username": "...", "email": "...", "role": "..."}`
- staticmethod `is_valid_email(email: str) -> bool`: returns True if email contains "@" and "."
"""

# I AM NOT DONE

# Concept Tip: `@classmethod` is Python's standard way to write named alternative constructors.


class User:
    # TODO: implement
    pass


# ---------------------------------------------------------------- tests


def test_user_factories():
    u1 = User.from_csv_line("bob,bob@example.com,admin")
    assert u1.username == "bob"
    assert u1.email == "bob@example.com"
    assert u1.role == "admin"

    u2 = User.from_dict({"username": "charlie", "email": "c@test.org"})
    assert u2.username == "charlie"
    assert u2.role == "member"

    assert User.is_valid_email("test@example.com") is True
    assert User.is_valid_email("bad_email") is False
