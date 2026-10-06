# 12 Linked Lists (NeetCode)

### The Mental Model: Pointers and Memory
Unlike contiguous arrays, linked list nodes are scattered across heap memory. Each node holds data and a reference (`next`) to the next node.
- **The Dummy Node Trick:** Creating a fake head node `dummy = ListNode(0); dummy.next = head` eliminates edge cases when modifying the head of a list.
- **Floyd's Tortoise & Hare:** A slow pointer advancing 1 step and a fast pointer advancing 2 steps detect cycles in $O(n)$ time and $O(1)$ space.
