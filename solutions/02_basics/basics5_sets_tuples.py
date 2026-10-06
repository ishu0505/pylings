"""
basics5_sets_tuples — Solution
"""


def common_and_unique(set_a: set[int], set_b: set[int]) -> tuple[set[int], set[int]]:
    return (set_a & set_b, set_a ^ set_b)


def dedupe_preserve_order(items: list[int]) -> list[int]:
    seen = set()
    result = []
    for x in items:
        if x not in seen:
            seen.add(x)
            result.append(x)
    return result


# ---------------------------------------------------------------- tests


def test_common_and_unique():
    a = {1, 2, 3}
    b = {2, 3, 4}
    common, unique = common_and_unique(a, b)
    assert common == {2, 3}
    assert unique == {1, 4}


def test_dedupe_preserve_order():
    nums = [4, 5, 4, 1, 5, 2, 1, 3]
    assert dedupe_preserve_order(nums) == [4, 5, 1, 2, 3]
    assert dedupe_preserve_order([]) == []
