"""
longest_repeating_character_replacement — Solution
"""
from collections import defaultdict


def character_replacement(s: str, k: int) -> int:
    counts: dict[str, int] = defaultdict(int)
    l = 0
    max_f = 0
    best = 0
    for r in range(len(s)):
        counts[s[r]] += 1
        max_f = max(max_f, counts[s[r]])
        while (r - l + 1) - max_f > k:
            counts[s[l]] -= 1
            l += 1
        best = max(best, r - l + 1)
    return best


# ---------------------------------------------------------------- tests


def test_character_replacement():
    assert character_replacement("ABAB", 2) == 4
    assert character_replacement("AABABBA", 1) == 4
    assert character_replacement("AAAA", 0) == 4
