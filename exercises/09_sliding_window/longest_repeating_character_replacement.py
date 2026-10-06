"""
longest_repeating_character_replacement — Longest Repeating Char Replacement (NeetCode) difficulty: medium

You are given a string s and an integer k. You can choose any character and change it
to any other uppercase English character at most k times. Return length of longest substring
containing the same letter you can get.
Goal: O(n) time.
"""

# I AM NOT DONE

# Concept Tip: `(window_length - max_frequency)` tells you how many characters must be flipped.
from collections import defaultdict


def character_replacement(s: str, k: int) -> int:
    # TODO: implement in O(n)
    raise NotImplementedError


# ---------------------------------------------------------------- tests


def test_character_replacement():
    assert character_replacement("ABAB", 2) == 4
    assert character_replacement("AABABBA", 1) == 4
    assert character_replacement("AAAA", 0) == 4
