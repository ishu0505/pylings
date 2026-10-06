# 19 Tries / Prefix Trees (NeetCode)

### The Mental Model: Trees of Dictionaries
A Trie is a tree where each node holds a dictionary mapping characters to child nodes `children: dict[str, TrieNode]` and a flag `is_end_of_word: bool`.
- Inserting and searching for a word of length $L$ runs in **$O(L)$ time**, independent of the number of words stored in the dictionary!
- Used extensively in search engines, autocomplete systems, and spelling checkers.
