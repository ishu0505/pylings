"""
valid_parentheses — Solution
"""


def is_valid(s: str) -> bool:
    stack = []
    pairs = {")": "(", "}": "{", "]": "["}
    for c in s:
        if c in pairs:
            if not stack or stack.pop() != pairs[c]:
                return False
        else:
            stack.append(c)
    return len(stack) == 0


# ---------------------------------------------------------------- tests


def test_valid_parentheses():
    assert is_valid("()") is True
    assert is_valid("()[]{}") is True
    assert is_valid("(]") is False
    assert is_valid("([)]") is False
    assert is_valid("{[]}") is True
    assert is_valid("]") is False
