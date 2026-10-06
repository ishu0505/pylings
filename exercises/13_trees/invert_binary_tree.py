"""
invert_binary_tree — Invert Binary Tree (NeetCode)     difficulty: easy

Given the root of a binary tree, invert the tree, and return its root.
Goal: O(n) time, O(h) space where h is tree height.
"""

# I AM NOT DONE

# Concept Tip: Inverting a tree is simply mirroring left and right child pointers at every level.


class TreeNode:
    def __init__(self, val: int = 0, left: "TreeNode | None" = None, right: "TreeNode | None" = None) -> None:
        self.val = val
        self.left = left
        self.right = right


def invert_tree(root: TreeNode | None) -> TreeNode | None:
    # TODO: implement
    raise NotImplementedError


# ---------------------------------------------------------------- tests


def test_invert():
    root = TreeNode(4, TreeNode(2, TreeNode(1), TreeNode(3)), TreeNode(7, TreeNode(6), TreeNode(9)))
    inv = invert_tree(root)
    assert inv.val == 4
    assert inv.left.val == 7
    assert inv.right.val == 2
    assert inv.left.left.val == 9
