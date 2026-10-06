"""
validate_binary_search_tree — Validate BST (NeetCode)   difficulty: medium

Given the root of a binary tree, determine if it is a valid binary search tree (BST).
Goal: O(n) time.
"""

# I AM NOT DONE

# Concept Tip: Checking only immediate children is insufficient; whole subtrees must satisfy upper and lower bounds.


class TreeNode:
    def __init__(self, val: int = 0, left: "TreeNode | None" = None, right: "TreeNode | None" = None) -> None:
        self.val = val
        self.left = left
        self.right = right


def is_valid_bst(root: TreeNode | None) -> bool:
    # TODO: implement
    raise NotImplementedError


# ---------------------------------------------------------------- tests


def test_is_valid_bst():
    valid = TreeNode(2, TreeNode(1), TreeNode(3))
    assert is_valid_bst(valid) is True

    invalid = TreeNode(5, TreeNode(1), TreeNode(4, TreeNode(3), TreeNode(6)))
    assert is_valid_bst(invalid) is False
