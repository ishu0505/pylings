"""
design_add_and_search_words — Add and Search Words (NeetCode) difficulty: medium

Design a data structure that supports adding new words and finding if a string matches any previously added string.
`search(word)` can contain '.' which matches any letter.
"""

# I AM NOT DONE

# Concept Tip: '.' is a wildcard branch exploring all child nodes.


class WordDictionary:
    # TODO: implement
    pass


# ---------------------------------------------------------------- tests


def test_word_dictionary():
    wd = WordDictionary()
    wd.add_word("bad")
    wd.add_word("dad")
    wd.add_word("mad")
    assert wd.search("pad") is False
    assert wd.search("bad") is True
    assert wd.search(".ad") is True
    assert wd.search("b..") is True
