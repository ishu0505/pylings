"""
basics3_loops_control — Solution
"""


def indexed_items(items: list[str], start: int = 1) -> list[str]:
    return [f"{i}. {item}" for i, item in enumerate(items, start=start)]


def dot_product(vec1: list[int], vec2: list[int]) -> int:
    return sum(a * b for a, b in zip(vec1, vec2))


# ---------------------------------------------------------------- tests


def test_indexed_items():
    assert indexed_items(["first", "second"]) == ["1. first", "2. second"]
    assert indexed_items(["only"], start=0) == ["0. only"]
    assert indexed_items([]) == []


def test_dot_product():
    assert dot_product([1, 2, 3], [4, 5, 6]) == 32
    assert dot_product([0, 1], [10, 20]) == 20
    assert dot_product([], []) == 0
