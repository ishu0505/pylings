"""
time_based_key_value_store — Solution
"""
from collections import defaultdict


class TimeMap:
    def __init__(self) -> None:
        self.store: dict[str, list[tuple[int, str]]] = defaultdict(list)

    def set(self, key: str, value: str, timestamp: int) -> None:
        self.store[key].append((timestamp, value))

    def get(self, key: str, timestamp: int) -> str:
        values = self.store.get(key, [])
        if not values:
            return ""

        lo, hi = 0, len(values) - 1
        res = ""
        while lo <= hi:
            mid = (lo + hi) // 2
            if values[mid][0] <= timestamp:
                res = values[mid][1]
                lo = mid + 1
            else:
                hi = mid - 1
        return res


# ---------------------------------------------------------------- tests


def test_time_map():
    tm = TimeMap()
    tm.set("foo", "bar", 1)
    assert tm.get("foo", 1) == "bar"
    assert tm.get("foo", 3) == "bar"
    tm.set("foo", "bar2", 4)
    assert tm.get("foo", 4) == "bar2"
    assert tm.get("foo", 5) == "bar2"
    assert tm.get("foo", 0) == ""
