"""
longest_substring_without_repeating — Longest Substring Without Repeating (NeetCode) difficulty: medium

Given a string s, find the length of the longest substring without repeating characters.
Goal: O(n) time, O(min(m, n)) space.
"""

# I AM NOT DONE

# Concept Tip: When a duplicate appears at `r`, shrink from `l` until the duplicate is evicted.


def length_of_longest_substring(s: str) -> int:
    # TODO: implement in O(n)
    raise NotImplementedError


# ---------------------------------------------------------------- tests


def test_longest_substring():
    assert length_of_longest_substring("abcabcbb") == 3
    assert length_of_longest_substring("bbbbb") == 1
    assert length_of_longest_substring("pwwkew") == 3
    assert length_of_longest_substring("") == 0
