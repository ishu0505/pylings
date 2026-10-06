"""
combination_sum — Combination Sum (NeetCode)           difficulty: medium

Given an array of distinct integers candidates and a target integer target,
return a list of all unique combinations of candidates where the chosen numbers sum to target.
The same number may be chosen an unlimited number of times.
"""

# I AM NOT DONE

# Concept Tip: Pass the same index `i` to allow repeating an element, or `i + 1` to move on.


def combination_sum(candidates: list[int], target: int) -> list[list[int]]:
    # TODO: implement
    raise NotImplementedError


# ---------------------------------------------------------------- tests


def test_combination_sum():
    res = combination_sum([2, 3, 6, 7], 7)
    sorted_res = sorted([sorted(c) for c in res])
    assert sorted_res == [[2, 2, 3], [7]]
    assert combination_sum([2], 1) == []
