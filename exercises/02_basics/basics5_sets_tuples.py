"""
basics5_sets_tuples — Sets and Tuples                 difficulty: easy

Implement:
1. `common_and_unique(set_a: set[int], set_b: set[int]) -> tuple[set[int], set[int]]`:
   returns a tuple (intersection, symmetric_difference).
2. `dedupe_preserve_order(items: list[int]) -> list[int]`:
   returns unique items preserving the original first-occurrence order in O(n) time.
"""

# I AM NOT DONE

# Concept Tip: Sets give O(1) membership checks. In Python 3.7+, dict keys preserve insertion order.


def common_and_unique(set_a: set[int], set_b: set[int]) -> tuple[set[int], set[int]]:
    # TODO: implement
    raise NotImplementedError


def dedupe_preserve_order(items: list[int]) -> list[int]:
    # TODO: implement
    raise NotImplementedError


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
