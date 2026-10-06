"""
permutations — Permutations (NeetCode)                 difficulty: medium

Given an array nums of distinct integers, return all the possible permutations.
Goal: O(n! * n) time.
"""

# I AM NOT DONE

# Concept Tip: For n elements, there are n choices for the first position, (n-1) for the second, etc. (n!).


def permute(nums: list[int]) -> list[list[int]]:
    # TODO: implement
    raise NotImplementedError


# ---------------------------------------------------------------- tests


def test_permutations():
    res = permute([1, 2, 3])
    assert len(res) == 6
    assert [1, 2, 3] in res
    assert [3, 2, 1] in res
    assert permute([1]) == [[1]]
