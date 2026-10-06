"""
diag1_first_unique — First Unique Character       difficulty: easy

Given a string s, return the index of the first non-repeating character.
If every character repeats, return -1.
Goal: O(n) time, O(1) auxiliary space (character set <= 26).
"""

# I AM NOT DONE

# Concept Tip: A single-pass removal trick fails on 3+ repeats ('aaa' vs 'aaab').
# Two passes with a frequency count is clean and optimal.


def first_unique_char(s: str) -> int:
    # TODO: implement
    raise NotImplementedError


# ---------------------------------------------------------------- tests


def test_first_unique_char():
    assert first_unique_char("leetcode") == 0
    assert first_unique_char("loveleetcode") == 2
    assert first_unique_char("aabb") == -1
    assert first_unique_char("aaa") == -1
    assert first_unique_char("aaab") == 3
    assert first_unique_char("") == -1
