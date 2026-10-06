"""
search_2d_matrix — Search a 2D Matrix (NeetCode)       difficulty: medium

You are given an m x n integer matrix with the following properties:
- Each row is sorted in non-decreasing order.
- The first integer of each row is greater than the last integer of the previous row.
Given target, return true if target is in matrix or false otherwise.
Goal: O(log(m * n)) time.
"""

# I AM NOT DONE

# Concept Tip: Virtual index `i` maps to `matrix[i // cols][i % cols]`.


def search_matrix(matrix: list[list[int]], target: int) -> bool:
    # TODO: implement in O(log(m * n))
    raise NotImplementedError


# ---------------------------------------------------------------- tests


def test_search_matrix():
    mat = [[1, 3, 5, 7], [10, 11, 16, 20], [23, 30, 34, 60]]
    assert search_matrix(mat, 3) is True
    assert search_matrix(mat, 13) is False
    assert search_matrix([], 1) is False
