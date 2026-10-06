"""
permutation_in_string — Permutation in String (NeetCode) difficulty: medium

Given two strings s1 and s2, return true if s2 contains a permutation of s1, or false otherwise.
Goal: O(len(s1) + len(s2)) time.
"""

# I AM NOT DONE

# Concept Tip: When the window size is constant `k = len(s1)`, adding `s2[i]` and removing `s2[i - k]` gives O(1) window updates.
from collections import Counter


def check_inclusion(s1: str, s2: str) -> bool:
    # TODO: implement
    raise NotImplementedError


# ---------------------------------------------------------------- tests


def test_permutation():
    assert check_inclusion("ab", "eidbaooo") is True
    assert check_inclusion("ab", "eidboaoo") is False
    assert check_inclusion("adc", "dcda") is True
