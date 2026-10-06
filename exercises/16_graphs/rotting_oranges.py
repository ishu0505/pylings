"""
rotting_oranges — Rotting Oranges (NeetCode)           difficulty: medium

You are given an m x n grid where each cell has: 0 (empty), 1 (fresh), 2 (rotten).
Every minute, any fresh orange that is 4-directionally adjacent to a rotten orange becomes rotten.
Return the minimum number of minutes until no cell has a fresh orange, or -1 if impossible.
Goal: O(m * n) time.
"""

# I AM NOT DONE

# Concept Tip: Multi-source BFS begins with all starting points simultaneously queued at t=0.
from collections import deque


def oranges_rotting(grid: list[list[int]]) -> int:
    # TODO: implement
    raise NotImplementedError


# ---------------------------------------------------------------- tests


def test_rotting_oranges():
    grid = [[2, 1, 1], [1, 1, 0], [0, 1, 1]]
    assert oranges_rotting(grid) == 4

    grid2 = [[2, 1, 1], [0, 1, 1], [1, 0, 1]]
    assert oranges_rotting(grid2) == -1

    grid3 = [[0, 2]]
    assert oranges_rotting(grid3) == 0
