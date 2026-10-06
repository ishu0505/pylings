"""
diag1_first_unique — Solution
"""
from collections import Counter


def first_unique_char(s: str) -> int:
    counts = Counter(s)
    for idx, char in enumerate(s):
        if counts[char] == 1:
            return idx
    return -1


# ---------------------------------------------------------------- tests


def test_first_unique_char():
    assert first_unique_char("leetcode") == 0
    assert first_unique_char("loveleetcode") == 2
    assert first_unique_char("aabb") == -1
    assert first_unique_char("aaa") == -1
    assert first_unique_char("aaab") == 3
    assert first_unique_char("") == -1
