"""
diag3_stack_class — Stack wrapping a list + dunders   difficulty: medium

Build a Stack class that:
- maintains internal elements in a list
- has methods: push(item), pop() -> item, peek() -> item, is_empty() -> bool
- raises IndexError("stack is empty") when popping or peeking an empty stack
- implements __len__, __bool__, and __repr__ (e.g. "Stack([1, 2])")
"""

# I AM NOT DONE

# Concept Tip: __len__ returns size; __bool__ defines truthiness; __repr__ is debugging string.


class Stack:
    def __init__(self) -> None:
        # TODO: initialize storage
        raise NotImplementedError

    def push(self, item: int) -> None:
        raise NotImplementedError

    def pop(self) -> int:
        raise NotImplementedError

    def peek(self) -> int:
        raise NotImplementedError

    def is_empty(self) -> bool:
        raise NotImplementedError

    def __len__(self) -> int:
        raise NotImplementedError

    def __bool__(self) -> bool:
        raise NotImplementedError

    def __repr__(self) -> str:
        raise NotImplementedError


# ---------------------------------------------------------------- tests
import pytest


def test_stack_basic():
    s = Stack()
    assert len(s) == 0
    assert not bool(s)
    assert s.is_empty()

    s.push(10)
    s.push(20)
    assert len(s) == 2
    assert bool(s)
    assert s.peek() == 20
    assert s.pop() == 20
    assert s.pop() == 10
    assert s.is_empty()


def test_stack_empty_errors():
    s = Stack()
    with pytest.raises(IndexError):
        s.pop()
    with pytest.raises(IndexError):
        s.peek()


def test_stack_repr():
    s = Stack()
    s.push(1)
    s.push(2)
    assert repr(s) == "Stack([1, 2])"
