"""
valid_anagram — Valid Anagram (NeetCode)               difficulty: easy

Given two strings s and t, return true if t is an anagram of s, and false otherwise.
Goal: O(n) time, O(1) auxiliary space (alphabet size <= 26).
"""

# I AM NOT DONE

# Concept Tip: Two words are anagrams if and only if their character frequency counts match exactly.


def is_anagram(s: str, t: str) -> bool:
    # TODO: implement
    raise NotImplementedError


# ---------------------------------------------------------------- tests


def test_valid_anagram():
    assert is_anagram("anagram", "nagaram") is True
    assert is_anagram("rat", "car") is False
    assert is_anagram("a", "ab") is False
    assert is_anagram("", "") is True
