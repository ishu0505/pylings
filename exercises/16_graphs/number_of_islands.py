"""
number_of_islands — Number of Islands (NeetCode)       difficulty: medium

Given an m x n 2D binary grid grid which represents a map of '1's (land) and '0's (water),
return the number of islands. An island is surrounded by water and formed by connecting adjacent lands.
Goal: O(m * n) time.
"""

# I AM NOT DONE

# Concept Tip: Flooding visited land cells with '0' avoids needing a separate visited set.


def num_islands(grid: list[list[str]]) -> int:
    # TODO: implement
    raise NotImplementedError


# ---------------------------------------------------------------- tests


def test_islands():
    g1 = [
        ["1", "1", "1", "1", "0"],
        ["1", "1", "0", "1", "0"],
        ["1", "1", "0", "0", "0"],
        ["0", "0", "0", "0", "0"],
    ]
    assert num_islands(g1) == 1

    g2 = [
        ["1", "1", "0", "0", "0"],
        ["1", "1", "0", "0", "0"],
        ["0", "0", "1", "0", "0"],
        ["0", "0", "0", "1", "1"],
    ]
    assert num_islands(g2) == 3
    assert num_islands([]) == 0
