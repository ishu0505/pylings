"""
merge_two_sorted_lists — Merge Two Sorted Lists (NeetCode) difficulty: easy

Merge the two sorted lists into one sorted list by splicing together their nodes.
Goal: O(n + m) time, O(1) auxiliary space.
"""

# I AM NOT DONE

# Concept Tip: `dummy.next` holds the true head of the merged result.


class ListNode:
    def __init__(self, val: int = 0, next: "ListNode | None" = None) -> None:
        self.val = val
        self.next = next


def merge_two_lists(list1: ListNode | None, list2: ListNode | None) -> ListNode | None:
    # TODO: implement
    raise NotImplementedError


# ---------------------------------------------------------------- tests


def to_arr(head):
    res = []
    while head:
        res.append(head.val)
        head = head.next
    return res


def test_merge():
    l1 = ListNode(1, ListNode(2, ListNode(4)))
    l2 = ListNode(1, ListNode(3, ListNode(4)))
    merged = merge_two_lists(l1, l2)
    assert to_arr(merged) == [1, 1, 2, 3, 4, 4]
