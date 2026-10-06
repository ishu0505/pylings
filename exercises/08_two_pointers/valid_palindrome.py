"""
valid_palindrome — Valid Palindrome (NeetCode)         difficulty: easy

A phrase is a palindrome if, after converting all uppercase letters into lowercase
and removing all non-alphanumeric characters, it reads the same forward and backward.
Goal: O(n) time, O(1) auxiliary space.
"""

# I AM NOT DONE

# Concept Tip: `str.isalnum()` checks if a character is a letter or number.


def is_palindrome(s: str) -> bool:
    # TODO: implement in O(n) time and O(1) space
    raise NotImplementedError


# ---------------------------------------------------------------- tests


def test_valid_palindrome():
    assert is_palindrome("A man, a plan, a canal: Panama") is True
    assert is_palindrome("race a car") is False
    assert is_palindrome(" ") is True
    assert is_palindrome("0P") is False
