"""
permutation_in_string — Solution
"""
from collections import Counter


def check_inclusion(s1: str, s2: str) -> bool:
    if len(s1) > len(s2):
        return False
    c1 = Counter(s1)
    k = len(s1)
    c2 = Counter(s2[:k])
    if c1 == c2:
        return True

    for i in range(k, len(s2)):
        c2[s2[i]] += 1
        c2[s2[i - k]] -= 1
        if c2[s2[i - k]] == 0:
            del c2[s2[i - k]]
        if c1 == c2:
            return True
    return False


# ---------------------------------------------------------------- tests


def test_permutation():
    assert check_inclusion("ab", "eidbaooo") is True
    assert check_inclusion("ab", "eidboaoo") is False
    assert check_inclusion("adc", "dcda") is True
