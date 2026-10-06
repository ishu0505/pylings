"""
basics6_dicts_mapping — Dict manipulation and grouping   difficulty: medium

Implement:
1. `group_by_length(words: list[str]) -> dict[int, list[str]]`:
   groups words by length using dict.setdefault.
2. `sort_dict_by_value(scores: dict[str, int]) -> list[tuple[str, int]]`:
   returns list of (name, score) sorted from highest score to lowest.
"""

# I AM NOT DONE

# Concept Tip: `d.setdefault(key, []).append(x)` is the classic idiom for building grouped lists.


def group_by_length(words: list[str]) -> dict[int, list[str]]:
    # TODO: implement
    raise NotImplementedError


def sort_dict_by_value(scores: dict[str, int]) -> list[tuple[str, int]]:
    # TODO: implement
    raise NotImplementedError


# ---------------------------------------------------------------- tests


def test_group_by_length():
    words = ["a", "bb", "c", "ddd", "ee"]
    assert group_by_length(words) == {
        1: ["a", "c"],
        2: ["bb", "ee"],
        3: ["ddd"],
    }
    assert group_by_length([]) == {}


def test_sort_dict_by_value():
    scores = {"alice": 85, "bob": 95, "charlie": 70}
    assert sort_dict_by_value(scores) == [("bob", 95), ("alice", 85), ("charlie", 70)]
