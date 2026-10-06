"""
oop6_protocol_abc — Structural typing with typing.Protocol   difficulty: medium

Define `Repository[T]` as a `typing.Protocol`:
- method `save(item: T) -> None`
- method `get_by_id(item_id: str) -> T | None`
- method `count() -> int`

Implement `InMemoryItemRepo`:
- stores items in an internal dict mapping `item["id"] -> item`.
- adheres to the Repository protocol without explicitly subclassing it!
"""

# I AM NOT DONE

# Concept Tip: `Protocol` allows duck typing with static type checker guarantees.
from typing import Any, Protocol, runtime_checkable


@runtime_checkable
class Repository(Protocol):
    # TODO: define protocol signatures
    pass


class InMemoryItemRepo:
    # TODO: implement
    pass


# ---------------------------------------------------------------- tests


def test_repository_protocol():
    repo = InMemoryItemRepo()
    assert isinstance(repo, Repository)

    assert repo.count() == 0
    repo.save({"id": "item-1", "name": "Item One"})
    assert repo.count() == 1
    assert repo.get_by_id("item-1") == {"id": "item-1", "name": "Item One"}
    assert repo.get_by_id("missing") is None
