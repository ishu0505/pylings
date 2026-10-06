"""
implement_trie — Implement Trie (NeetCode)             difficulty: medium

A trie (prefix tree) is a tree data structure used to store a dynamic set or associative array.
Implement Trie:
- `insert(word: str) -> None`: inserts word
- `search(word: str) -> bool`: returns True if word is in trie
- `starts_with(prefix: str) -> bool`: returns True if there is any word starting with prefix
"""

# I AM NOT DONE

# Concept Tip: Each node represents one character; root represents empty prefix.


class TrieNode:
    def __init__(self) -> None:
        self.children: dict[str, "TrieNode"] = {}
        self.is_word: bool = False


class Trie:
    # TODO: implement
    pass


# ---------------------------------------------------------------- tests


def test_trie():
    trie = Trie()
    trie.insert("apple")
    assert trie.search("apple") is True
    assert trie.search("app") is False
    assert trie.starts_with("app") is True
    trie.insert("app")
    assert trie.search("app") is True
