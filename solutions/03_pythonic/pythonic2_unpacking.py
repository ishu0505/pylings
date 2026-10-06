"""
pythonic2_unpacking — Solution
"""


def split_head_middle_tail(items: list[int]) -> tuple[int, list[int], int]:
    first, *middle, last = items
    return first, middle, last


def merge_configs(base: dict, override: dict) -> dict:
    return {**base, **override}


# ---------------------------------------------------------------- tests


def test_split():
    assert split_head_middle_tail([1, 2, 3, 4, 5]) == (1, [2, 3, 4], 5)
    assert split_head_middle_tail([10, 20]) == (10, [], 20)


def test_merge_configs():
    base = {"env": "prod", "port": 8000, "debug": False}
    override = {"port": 8080, "debug": True}
    res = merge_configs(base, override)
    assert res == {"env": "prod", "port": 8080, "debug": True}
    assert base["port"] == 8000
