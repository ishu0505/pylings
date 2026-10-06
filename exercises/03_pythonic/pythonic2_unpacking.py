"""
pythonic2_unpacking — Extended iterable unpacking       difficulty: easy

1. `split_head_middle_tail(items: list[int]) -> tuple[int, list[int], int]`:
   returns (first, middle_elements_list, last). Assume len(items) >= 2.
2. `merge_configs(base: dict, override: dict) -> dict`:
   returns a new dict where override values take precedence.
"""

# I AM NOT DONE

# Concept Tip: `first, *rest = items` binds the head to a variable and the rest to a list.


def split_head_middle_tail(items: list[int]) -> tuple[int, list[int], int]:
    # TODO: implement
    raise NotImplementedError


def merge_configs(base: dict, override: dict) -> dict:
    # TODO: implement
    raise NotImplementedError


# ---------------------------------------------------------------- tests


def test_split():
    assert split_head_middle_tail([1, 2, 3, 4, 5]) == (1, [2, 3, 4], 5)
    assert split_head_middle_tail([10, 20]) == (10, [], 20)


def test_merge_configs():
    base = {"env": "prod", "port": 8000, "debug": False}
    override = {"port": 8080, "debug": True}
    res = merge_configs(base, override)
    assert res == {"env": "prod", "port": 8080, "debug": True}
    assert base["port"] == 8000  # immutability: base was not modified
