"""
basics4_functions_args — Mutable defaults & keyword-only args   difficulty: medium

1. `append_item(item: int, target: list[int] | None = None) -> list[int]`:
   Appends item to target and returns target. If target is None, creates a fresh new list.
   Must NOT share state across calls when target is omitted!

2. `build_user(name: str, *tags: str, active: bool = True, **metadata) -> dict`:
   Returns a dict with: {"name": name, "tags": list(tags), "active": active, "metadata": metadata}.
   Notice `active` is keyword-only or optional with a default.
"""

# I AM NOT DONE

# Concept Tip: Default arguments are created once when the function is defined,
# not each time it is called. Defaulting to None prevents shared state bugs.


def append_item(item: int, target: list[int] | None = None) -> list[int]:
    # TODO: implement safely
    raise NotImplementedError


def build_user(name: str, *tags: str, active: bool = True, **metadata) -> dict:
    # TODO: implement
    raise NotImplementedError


# ---------------------------------------------------------------- tests


def test_append_item_fresh_each_time():
    first = append_item(1)
    second = append_item(2)
    assert first == [1]
    assert second == [2]  # Should NOT be [1, 2]!


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
