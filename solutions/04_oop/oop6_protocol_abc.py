"""
oop6_protocol_abc — Solution
"""
from typing import Any, Protocol, runtime_checkable


@runtime_checkable
class Repository(Protocol):
    def save(self, item: dict[str, Any]) -> None:
        ...

    def get_by_id(self, item_id: str) -> dict[str, Any] | None:
        ...

    def count(self) -> int:
        ...


class InMemoryItemRepo:
    def __init__(self) -> None:
        self._store: dict[str, dict[str, Any]] = {}

    def save(self, item: dict[str, Any]) -> None:
        self._store[item["id"]] = item

    def get_by_id(self, item_id: str) -> dict[str, Any] | None:
        return self._store.get(item_id)

    def count(self) -> int:
        return len(self._store)


# ---------------------------------------------------------------- tests


def test_repository_protocol():
    repo = InMemoryItemRepo()
    assert isinstance(repo, Repository)

    assert repo.count() == 0
    repo.save({"id": "item-1", "name": "Item One"})
    assert repo.count() == 1
    assert repo.get_by_id("item-1") == {"id": "item-1", "name": "Item One"}
    assert repo.get_by_id("missing") is None
