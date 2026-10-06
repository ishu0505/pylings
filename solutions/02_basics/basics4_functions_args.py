"""
basics4_functions_args — Solution
"""


def append_item(item: int, target: list[int] | None = None) -> list[int]:
    if target is None:
        target = []
    target.append(item)
    return target


def build_user(name: str, *tags: str, active: bool = True, **metadata) -> dict:
    return {
        "name": name,
        "tags": list(tags),
        "active": active,
        "metadata": metadata,
    }


# ---------------------------------------------------------------- tests


def test_append_item_fresh_each_time():
    first = append_item(1)
    second = append_item(2)
    assert first == [1]
    assert second == [2]


def test_append_item_with_existing():
    existing = [10, 20]
    result = append_item(30, existing)
    assert result == [10, 20, 30]
    assert result is existing


def test_build_user():
    user = build_user("Alice", "admin", "dev", active=False, team="AI", role="engineer")
    assert user == {
        "name": "Alice",
        "tags": ["admin", "dev"],
        "active": False,
        "metadata": {"team": "AI", "role": "engineer"},
    }
