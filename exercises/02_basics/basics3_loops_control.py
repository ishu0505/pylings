"""
basics3_loops_control — Enumerate & Zip              difficulty: easy

Implement:
1. `indexed_items(items: list[str], start: int = 1) -> list[str]`:
   returns list like ["1. apple", "2. banana"] using enumerate.
2. `dot_product(vec1: list[int], vec2: list[int]) -> int`:
   computes the dot product of two vectors of equal length using zip.
"""

# I AM NOT DONE

# Concept Tip: `zip` pairs up elements; `enumerate` produces (index, item) tuples.


def indexed_items(items: list[str], start: int = 1) -> list[str]:
    # TODO: implement
    raise NotImplementedError


def dot_product(vec1: list[int], vec2: list[int]) -> int:
    # TODO: implement
    raise NotImplementedError


# ---------------------------------------------------------------- tests


def test_indexed_items():
    assert indexed_items(["first", "second"]) == ["1. first", "2. second"]
    assert indexed_items(["only"], start=0) == ["0. only"]
    assert indexed_items([]) == []


def test_dot_product():
    assert dot_product([1, 2, 3], [4, 5, 6]) == 32  # 1*4 + 2*5 + 3*6 = 4 + 10 + 18
    assert dot_product([0, 1], [10, 20]) == 20
    assert dot_product([], []) == 0
