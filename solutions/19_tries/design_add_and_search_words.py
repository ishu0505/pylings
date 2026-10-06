"""
design_add_and_search_words — Solution
"""


class Node:
    def __init__(self) -> None:
        self.children: dict[str, "Node"] = {}
        self.is_word: bool = False


class WordDictionary:
    def __init__(self) -> None:
        self.root = Node()

    def add_word(self, word: str) -> None:
        curr = self.root
        for c in word:
            if c not in curr.children:
                curr.children[c] = Node()
            curr = curr.children[c]
        curr.is_word = True

    def search(self, word: str) -> bool:
        def dfs(j: int, root: Node) -> bool:
            curr = root
            for i in range(j, len(word)):
                c = word[i]
                if c == ".":
                    for child in curr.children.values():
                        if dfs(i + 1, child):
                            return True
                    return False
                else:
                    if c not in curr.children:
                        return False
                    curr = curr.children[c]
            return curr.is_word

        return dfs(0, self.root)


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
