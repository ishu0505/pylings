"""
oop4_class_static_methods — Solution
"""


class User:
    def __init__(self, username: str, email: str, role: str = "member") -> None:
        self.username = username
        self.email = email
        self.role = role

    @classmethod
    def from_csv_line(cls, line: str) -> "User":
        parts = [p.strip() for p in line.split(",")]
        role = parts[2] if len(parts) > 2 else "member"
        return cls(parts[0], parts[1], role)

    @classmethod
    def from_dict(cls, data: dict) -> "User":
        return cls(
            username=data["username"],
            email=data["email"],
            role=data.get("role", "member"),
        )

    @staticmethod
    def is_valid_email(email: str) -> bool:
        return "@" in email and "." in email


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
