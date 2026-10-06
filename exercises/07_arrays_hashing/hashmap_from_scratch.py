"""
hashmap_from_scratch — Build a HashMap from Scratch    difficulty: hard

Implement `MyHashMap`:
- `__init__(self, capacity: int = 4)`
- `put(self, key: str, value: int) -> None`: inserts or updates key. Resizes (doubles capacity) when load factor > 0.75!
- `get(self, key: str) -> int | None`: returns value or None if missing
- `remove(self, key: str) -> bool`: removes key; returns True if removed, False if not found
- `__len__(self) -> int`: number of active keys
- `__contains__(self, key: str) -> bool`
"""

# I AM NOT DONE

# Concept Tip: Separate chaining handles collisions by keeping a small linked list or array at each bucket.


class MyHashMap:
    # TODO: implement
    pass


# ---------------------------------------------------------------- tests


def test_hashmap_basic():
    hm = MyHashMap(capacity=4)
    assert len(hm) == 0
    assert hm.get("apple") is None

    hm.put("apple", 10)
    hm.put("banana", 20)
    assert len(hm) == 2
    assert hm.get("apple") == 10
    assert "banana" in hm

    # Update existing
    hm.put("apple", 15)
    assert hm.get("apple") == 15
    assert len(hm) == 2

    # Remove
    assert hm.remove("banana") is True
    assert "banana" not in hm
    assert len(hm) == 1
    assert hm.remove("missing") is False


def test_hashmap_resizing():
    hm = MyHashMap(capacity=4)
    # Inserting 4 items triggers resize (load factor 4/4 = 1.0 > 0.75)
    for i in range(10):
        hm.put(f"key_{i}", i * 100)
    assert len(hm) == 10
    for i in range(10):
        assert hm.get(f"key_{i}") == i * 100
