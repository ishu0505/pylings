"""
diag2_top_k_words — Solution
"""
from collections import Counter


def top_k_frequent_words(words: list[str], k: int) -> list[str]:
    counts = Counter(words)
    # Sort by -count, then alphabetically by word
    sorted_words = sorted(counts.keys(), key=lambda w: (-counts[w], w))
    return sorted_words[:k]


# ---------------------------------------------------------------- tests


def test_top_k_frequent_words():
    words = ["i", "love", "python", "i", "love", "coding"]
    assert top_k_frequent_words(words, 2) == ["i", "love"]

    words2 = ["the", "day", "is", "sunny", "the", "the", "the", "sunny", "is", "is"]
    assert top_k_frequent_words(words2, 4) == ["the", "is", "sunny", "day"]
