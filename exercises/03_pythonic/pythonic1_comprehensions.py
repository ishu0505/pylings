"""
pythonic1_comprehensions — Comprehensions               difficulty: easy

1. `even_squares(nums: list[int]) -> list[int]`:
   returns the squares of even numbers in nums.
2. `invert_dict(d: dict[str, int]) -> dict[int, str]`:
   inverts unique key-value pairs using a dict comprehension.
3. `flatten_matrix(matrix: list[list[int]]) -> list[int]`:
   flattens a 2D list into 1D using a nested list comprehension.
"""

# I AM NOT DONE

# Concept Tip: List comprehensions replace map/filter with clean, readable syntax.


def even_squares(nums: list[int]) -> list[int]:
    # TODO: implement
    raise NotImplementedError


def invert_dict(d: dict[str, int]) -> dict[int, str]:
    # TODO: implement
    raise NotImplementedError


def flatten_matrix(matrix: list[list[int]]) -> list[int]:
    # TODO: implement
    raise NotImplementedError


# ---------------------------------------------------------------- tests


def test_even_squares():
    assert even_squares([1, 2, 3, 4, 5, 6]) == [4, 16, 36]
    assert even_squares([1, 3, 5]) == []


def test_invert_dict():
    original = {"a": 1, "b": 2, "c": 3}
    assert invert_dict(original) == {1: "a", 2: "b", 3: "c"}


def test_flatten_matrix():
    matrix = [[1, 2], [3, 4, 5], [6]]
    assert flatten_matrix(matrix) == [1, 2, 3, 4, 5, 6]
    assert flatten_matrix([]) == []
