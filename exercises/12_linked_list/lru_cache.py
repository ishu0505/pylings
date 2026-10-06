"""
lru_cache — LRU Cache (NeetCode)                       difficulty: hard

Design a data structure that follows the constraints of a Least Recently Used (LRU) cache.
Implement LRUCache:
- `__init__(capacity: int)`
- `get(key: int) -> int`: return value if key exists, else -1. Moves node to most recent.
- `put(key: int, value: int) -> None`: update or insert. If capacity exceeded, evict LRU key.
All operations must run in O(1) average time!
"""

# I AM NOT DONE

# Concept Tip: Hash map gives O(1) find; doubly linked list gives O(1) node relocation.


class DNode:
    def __init__(self, key: int = 0, val: int = 0) -> None:
        self.key = key
        self.val = val
        self.prev: "DNode | None" = None
        self.next: "DNode | None" = None


class LRUCache:
    # TODO: implement
    pass


# ---------------------------------------------------------------- tests


def test_lru_cache():
    cache = LRUCache(2)
    cache.put(1, 1)
    cache.put(2, 2)
    assert cache.get(1) == 1       # returns 1, makes 1 most recently used
    cache.put(3, 3)                # evicts key 2
    assert cache.get(2) == -1      # not found
    cache.put(4, 4)                # evicts key 1
    assert cache.get(1) == -1      # not found
    assert cache.get(3) == 3       # returns 3
    assert cache.get(4) == 4       # returns 4
