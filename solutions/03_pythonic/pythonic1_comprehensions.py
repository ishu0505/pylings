"""
pythonic1_comprehensions — Solution
"""


def even_squares(nums: list[int]) -> list[int]:
    return [x * x for x in nums if x % 2 == 0]


def invert_dict(d: dict[str, int]) -> dict[int, str]:
    return {v: k for k, v in d.items()}


def flatten_matrix(matrix: list[list[int]]) -> list[int]:
    return [x for row in matrix for x in row]


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
