"""
linked_list_from_scratch — Solution
"""


class Node:
    def __init__(self, val: int, next: "Node | None" = None) -> None:
        self.val = val
        self.next = next


class LinkedList:
    def __init__(self) -> None:
        self.head: Node | None = None
        self.tail: Node | None = None
        self._size = 0

    def __len__(self) -> int:
        return self._size

    def append(self, val: int) -> None:
        new_node = Node(val)
        if not self.head:
            self.head = self.tail = new_node
        else:
            assert self.tail is not None
            self.tail.next = new_node
            self.tail = new_node
        self._size += 1

    def prepend(self, val: int) -> None:
        new_node = Node(val, self.head)
        self.head = new_node
        if not self.tail:
            self.tail = new_node
        self._size += 1

    def pop_front(self) -> int:
        if not self.head:
            raise IndexError("pop from empty list")
        val = self.head.val
        self.head = self.head.next
        self._size -= 1
        if not self.head:
            self.tail = None
        return val

    def to_list(self) -> list[int]:
        res = []
        curr = self.head
        while curr:
            res.append(curr.val)
            curr = curr.next
        return res


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
