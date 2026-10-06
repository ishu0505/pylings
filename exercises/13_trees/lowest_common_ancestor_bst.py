"""
lowest_common_ancestor_bst — LCA of BST (NeetCode)     difficulty: medium

Given a binary search tree (BST), find the lowest common ancestor (LCA) node of two given nodes p and q.
Goal: O(h) time, O(1) space.
"""

# I AM NOT DONE

# Concept Tip: The LCA in a BST is the first node where the search paths for p and q diverge.


class TreeNode:
    def __init__(self, val: int = 0, left: "TreeNode | None" = None, right: "TreeNode | None" = None) -> None:
        self.val = val
        self.left = left
        self.right = right


def lowest_common_ancestor(root: TreeNode, p: TreeNode, q: TreeNode) -> TreeNode:
    # TODO: implement
    raise NotImplementedError


# ---------------------------------------------------------------- tests


def test_lca_bst():
    p = TreeNode(2)
    q = TreeNode(8)
    root = TreeNode(6, p, q)
    assert lowest_common_ancestor(root, p, q).val == 6
