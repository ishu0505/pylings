"""
linked_list_cycle — Linked List Cycle (NeetCode)       difficulty: easy

Given head, the head of a linked list, determine if the linked list has a cycle in it.
Goal: O(n) time, O(1) space.
"""

# I AM NOT DONE

# Concept Tip: If a cycle exists, the fast runner will always lap the slow runner.


class ListNode:
    def __init__(self, val: int = 0, next: "ListNode | None" = None) -> None:
        self.val = val
        self.next = next


def has_cycle(head: ListNode | None) -> bool:
    # TODO: implement
    raise NotImplementedError


# ---------------------------------------------------------------- tests


def test_cycle():
    n1 = ListNode(3)
    n2 = ListNode(2)
    n3 = ListNode(0)
    n4 = ListNode(-4)
    n1.next, n2.next, n3.next, n4.next = n2, n3, n4, n2  # cycle back to n2
    assert has_cycle(n1) is True

    single = ListNode(1)
    assert has_cycle(single) is False
    assert has_cycle(None) is False
