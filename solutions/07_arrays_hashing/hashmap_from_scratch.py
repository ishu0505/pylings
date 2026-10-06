"""
hashmap_from_scratch — Solution
"""


class MyHashMap:
    def __init__(self, capacity: int = 4) -> None:
        self._capacity = max(1, capacity)
        self._size = 0
        self._buckets: list[list[list]] = [[] for _ in range(self._capacity)]

    def _hash(self, key: str) -> int:
        return hash(key) % self._capacity

    def _resize(self) -> None:
        old_buckets = self._buckets
        self._capacity *= 2
        self._buckets = [[] for _ in range(self._capacity)]
        self._size = 0
        for bucket in old_buckets:
            for k, v in bucket:
                self.put(k, v)

    def put(self, key: str, value: int) -> None:
        if (self._size + 1) / self._capacity > 0.75:
            self._resize()
        idx = self._hash(key)
        for pair in self._buckets[idx]:
            if pair[0] == key:
                pair[1] = value
                return
        self._buckets[idx].append([key, value])
        self._size += 1

    def get(self, key: str) -> int | None:
        idx = self._hash(key)
        for k, v in self._buckets[idx]:
            if k == key:
                return v
        return None

    def remove(self, key: str) -> bool:
        idx = self._hash(key)
        bucket = self._buckets[idx]
        for i, (k, _) in enumerate(bucket):
            if k == key:
                bucket.pop(i)
                self._size -= 1
                return True
        return False

    def __len__(self) -> int:
        return self._size

    def __contains__(self, key: str) -> bool:
        return self.get(key) is not None


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

    hm.put("apple", 15)
    assert hm.get("apple") == 15
    assert len(hm) == 2

    assert hm.remove("banana") is True
    assert "banana" not in hm
    assert len(hm) == 1
    assert hm.remove("missing") is False


def test_hashmap_resizing():
    hm = MyHashMap(capacity=4)
    for i in range(10):
        hm.put(f"key_{i}", i * 100)
    assert len(hm) == 10
    for i in range(10):
        assert hm.get(f"key_{i}") == i * 100
