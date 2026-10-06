"""
diag2_top_k_words — Top-K Frequent Words          difficulty: easy

Given a list of words and an integer k, return the k most frequent words.
Sort by frequency from highest to lowest. If two words have the same frequency,
tie-break by alphabetical order (e.g., "apple" before "banana").
"""

# I AM NOT DONE

# Concept Tip: Tuples compare element by element: (-freq, word) puts highest
# frequency first and breaks ties alphabetically.


def top_k_frequent_words(words: list[str], k: int) -> list[str]:
    # TODO: implement
    raise NotImplementedError


# ---------------------------------------------------------------- tests


def test_top_k_frequent_words():
    words = ["i", "love", "python", "i", "love", "coding"]
    assert top_k_frequent_words(words, 2) == ["i", "love"]

    words2 = ["the", "day", "is", "sunny", "the", "the", "the", "sunny", "is", "is"]
    assert top_k_frequent_words(words2, 4) == ["the", "is", "sunny", "day"]
