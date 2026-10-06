"""
valid_parentheses — Valid Parentheses (NeetCode)       difficulty: easy

Given a string s containing just the characters '(', ')', '{', '}', '[' and ']',
determine if the input string is valid.
Goal: O(n) time, O(n) space.
"""

# I AM NOT DONE

# Concept Tip: Every closing bracket must pair with the most recently opened bracket (LIFO).


def is_valid(s: str) -> bool:
    # TODO: implement
    raise NotImplementedError


# ---------------------------------------------------------------- tests


def test_valid_parentheses():
    assert is_valid("()") is True
    assert is_valid("()[]{}") is True
    assert is_valid("(]") is False
    assert is_valid("([)]") is False
    assert is_valid("{[]}") is True
    assert is_valid("]") is False
