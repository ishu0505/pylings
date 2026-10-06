"""
time_based_key_value_store — Time Based Key-Value Store (NeetCode) difficulty: medium

Design a time-based key-value data structure that can store multiple values for the same key
at different time stamps and retrieve the key's value at a certain timestamp.
- set(key, value, timestamp)
- get(key, timestamp): returns value with highest timestamp_prev <= timestamp, or "" if none.
"""

# I AM NOT DONE

# Concept Tip: `bisect` or standard binary search locates the rightmost timestamp <= query.


class TimeMap:
    # TODO: implement
    pass


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
