"""
group_anagrams — Group Anagrams (NeetCode)             difficulty: medium

Given an array of strings strs, group the anagrams together in any order.
Goal: O(m * n log n) or O(m * n) where m is number of strings and n is max string length.
"""

# I AM NOT DONE

# Concept Tip: Tuples are hashable in Python, so character count tuples make great dict keys.


def group_anagrams(strs: list[str]) -> list[list[str]]:
    # TODO: implement
    raise NotImplementedError


# ---------------------------------------------------------------- tests


def test_group_anagrams():
    input_strs = ["eat", "tea", "tan", "ate", "nat", "bat"]
    res = group_anagrams(input_strs)
    # Sort groups for deterministic comparison
    sorted_res = sorted([sorted(g) for g in res])
    expected = sorted([["bat"], ["nat", "tan"], ["ate", "eat", "tea"]])
    assert sorted_res == expected
    assert group_anagrams([""]) == [[""]]
    assert group_anagrams(["a"]) == [["a"]]
