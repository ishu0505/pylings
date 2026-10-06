"""
minimum_window_substring — Solution
"""
from collections import Counter


def min_window(s: str, t: str) -> str:
    if not t or not s:
        return ""
    target_counts = Counter(t)
    window_counts: dict[str, int] = {}
    have, need = 0, len(target_counts)
    res, min_len = (-1, -1), float("inf")
    l = 0

    for r, char in enumerate(s):
        window_counts[char] = window_counts.get(char, 0) + 1
        if char in target_counts and window_counts[char] == target_counts[char]:
            have += 1

        while have == need:
            if (r - l + 1) < min_len:
                min_len = r - l + 1
                res = (l, r)
            window_counts[s[l]] -= 1
            if s[l] in target_counts and window_counts[s[l]] < target_counts[s[l]]:
                have -= 1
            l += 1

    return s[res[0]:res[1] + 1] if min_len != float("inf") else ""


# ---------------------------------------------------------------- tests


def test_min_window():
    assert min_window("ADOBECODEBANC", "ABC") == "BANC"
    assert min_window("a", "a") == "a"
    assert min_window("a", "aa") == ""
