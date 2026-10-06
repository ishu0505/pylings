"""
reverse_linked_list — Reverse Linked List (NeetCode)    difficulty: easy

Given the head of a singly linked list, reverse the list, and return the reversed list.
Goal: O(n) time, O(1) auxiliary space.
"""

# I AM NOT DONE

# Concept Tip: Keep a temporary pointer to `curr.next` before overwriting it with `prev`.


class ListNode:
    def __init__(self, val: int = 0, next: "ListNode | None" = None) -> None:
        self.val = val
        self.next = next


def reverse_list(head: ListNode | None) -> ListNode | None:
    # TODO: implement
    raise NotImplementedError


# ---------------------------------------------------------------- tests


def to_arr(head):
    res = []
    while head:
        res.append(head.val)
        head = head.next
    return res


def test_reverse():
    h = ListNode(1, ListNode(2, ListNode(3)))
    rev = reverse_list(h)
    assert to_arr(rev) == [3, 2, 1]
    assert reverse_list(None) is None
