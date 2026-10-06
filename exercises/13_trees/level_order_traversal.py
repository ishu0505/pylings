"""
level_order_traversal — Level Order Traversal (NeetCode) difficulty: medium

Given the root of a binary tree, return the level order traversal of its nodes' values
(i.e., from left to right, level by level).
Goal: O(n) time, O(n) space.
"""

# I AM NOT DONE

# Concept Tip: Capturing `level_size = len(q)` at the start of the loop groups all nodes on that level.
from collections import deque


class TreeNode:
    def __init__(self, val: int = 0, left: "TreeNode | None" = None, right: "TreeNode | None" = None) -> None:
        self.val = val
        self.left = left
        self.right = right


def level_order(root: TreeNode | None) -> list[list[int]]:
    # TODO: implement
    raise NotImplementedError


# ---------------------------------------------------------------- tests


def test_level_order():
    root = TreeNode(3, TreeNode(9), TreeNode(20, TreeNode(15), TreeNode(7)))
    assert level_order(root) == [[3], [9, 20], [15, 7]]
    assert level_order(None) == []
