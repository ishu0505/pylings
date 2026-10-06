"""
reverse_linked_list — Solution
"""


class ListNode:
    def __init__(self, val: int = 0, next: "ListNode | None" = None) -> None:
        self.val = val
        self.next = next


def reverse_list(head: ListNode | None) -> ListNode | None:
    prev = None
    curr = head
    while curr:
        nxt = curr.next
        curr.next = prev
        prev = curr
        curr = nxt
    return prev


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
