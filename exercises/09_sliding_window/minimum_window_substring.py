"""
minimum_window_substring — Minimum Window Substring (NeetCode) difficulty: hard

Given two strings s and t of lengths m and n respectively, return the minimum window
substring of s such that every character in t (including duplicates) is included in the window.
If no such substring exists, return empty string "".
Goal: O(m + n) time.
"""

# I AM NOT DONE

# Concept Tip: Track how many distinct characters satisfy their target count with a `have` counter.
from collections import Counter


def min_window(s: str, t: str) -> str:
    # TODO: implement in O(m + n)
    raise NotImplementedError


# ---------------------------------------------------------------- tests


def test_min_window():
    assert min_window("ADOBECODEBANC", "ABC") == "BANC"
    assert min_window("a", "a") == "a"
    assert min_window("a", "aa") == ""
