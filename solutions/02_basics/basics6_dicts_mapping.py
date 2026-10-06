"""
basics6_dicts_mapping — Solution
"""


def group_by_length(words: list[str]) -> dict[int, list[str]]:
    res: dict[int, list[str]] = {}
    for w in words:
        res.setdefault(len(w), []).append(w)
    return res


def sort_dict_by_value(scores: dict[str, int]) -> list[tuple[str, int]]:
    return sorted(scores.items(), key=lambda kv: kv[1], reverse=True)


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
