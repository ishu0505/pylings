"""
subsets — Subsets (NeetCode)                           difficulty: medium

Given an integer array nums of unique elements, return all possible subsets (the power set).
The solution set must not contain duplicate subsets. Return the solution in any order.
Goal: O(n * 2^n) time.
"""

# I AM NOT DONE

# Concept Tip: The decision tree has depth n, and branching factor 2 at each step.


def subsets(nums: list[int]) -> list[list[int]]:
    # TODO: implement
    raise NotImplementedError


# ---------------------------------------------------------------- tests


def test_subsets():
    res = subsets([1, 2, 3])
    sorted_res = sorted([sorted(s) for s in res])
    expected = sorted([[], [1], [2], [3], [1, 2], [1, 3], [2, 3], [1, 2, 3]])
    assert sorted_res == expected
    assert subsets([]) == [[]]
