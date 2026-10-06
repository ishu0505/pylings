"""
group_anagrams — Solution
"""
from collections import defaultdict


def group_anagrams(strs: list[str]) -> list[list[str]]:
    groups: dict[tuple, list[str]] = defaultdict(list)
    for s in strs:
        key = tuple(sorted(s))
        groups[key].append(s)
    return list(groups.values())


# ---------------------------------------------------------------- tests


def test_group_anagrams():
    input_strs = ["eat", "tea", "tan", "ate", "nat", "bat"]
    res = group_anagrams(input_strs)
    sorted_res = sorted([sorted(g) for g in res])
    expected = sorted([["bat"], ["nat", "tan"], ["ate", "eat", "tea"]])
    assert sorted_res == expected
    assert group_anagrams([""]) == [[""]]
    assert group_anagrams(["a"]) == [["a"]]
