"""
linked_list_from_scratch — Build a Linked List from Scratch   difficulty: medium

Implement `LinkedList`:
- `append(val: int) -> None`: adds to the end in O(1) time
- `prepend(val: int) -> None`: adds to the front in O(1) time
- `pop_front() -> int`: removes and returns front value; raises IndexError if empty
- `to_list() -> list[int]`: converts to a standard Python list
- `__len__() -> int`
"""

# I AM NOT DONE

# Concept Tip: Maintaining a `tail` pointer allows O(1) appends to a singly linked list.


class Node:
    def __init__(self, val: int, next: "Node | None" = None) -> None:
        self.val = val
        self.next = next


class LinkedList:
    # TODO: implement
    pass


# ---------------------------------------------------------------- tests
import pytest


def test_linked_list_operations():
    ll = LinkedList()
    assert len(ll) == 0

    ll.append(2)
    ll.append(3)
    ll.prepend(1)
    assert len(ll) == 3
    assert ll.to_list() == [1, 2, 3]

    assert ll.pop_front() == 1
    assert ll.to_list() == [2, 3]
    assert len(ll) == 2


def test_linked_list_empty_pop():
    ll = LinkedList()
    with pytest.raises(IndexError):
        ll.pop_front()
