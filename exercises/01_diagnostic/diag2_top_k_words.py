"""
diag2_top_k_words — Top-K Frequent Words          difficulty: easy

Given a list of words and an integer k, return the k most frequent words.
Sort by frequency from highest to lowest. If two words have the same frequency,
tie-break by alphabetical order (e.g., "apple" before "banana").
"""


# Concept Tip: Tuples compare element by element: (-freq, word) puts highest
# frequency first and breaks ties alphabetically.


def top_k_frequent_words(words: list[str], k: int) -> list[str]:
    # TODO: implement
    w_map = {}
    for w in words:
        if w in w_map:
            w_map[w] = w_map[w] + 1
        else:
            w_map[w] = 1
    # print(w_map)


    new = sorted(w_map.items(), key=lambda pair: (-pair[1], pair[0]))[0:k]

    return [word for word, count in new]

    
  

# ---------------------------------------------------------------- tests


def test_top_k_frequent_words():
    words = ["i", "love", "python", "i", "love", "coding"]
    assert top_k_frequent_words(words, 2) == ["i", "love"]

    words2 = ["the", "day", "is", "sunny", "the", "the", "the", "sunny", "is", "is"]
    assert top_k_frequent_words(words2, 4) == ["the", "is", "sunny", "day"]
