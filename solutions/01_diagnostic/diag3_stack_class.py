"""
diag3_stack_class — Solution
"""


class Stack:
    def __init__(self) -> None:
        self._items: list[int] = []

    def push(self, item: int) -> None:
        self._items.append(item)

    def pop(self) -> int:
        if not self._items:
            raise IndexError("stack is empty")
        return self._items.pop()

    def peek(self) -> int:
        if not self._items:
            raise IndexError("stack is empty")
        return self._items[-1]

    def is_empty(self) -> bool:
        return len(self._items) == 0

    def __len__(self) -> int:
        return len(self._items)

    def __bool__(self) -> bool:
        return len(self._items) > 0

    def __repr__(self) -> str:
        return f"Stack({self._items!r})"


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
