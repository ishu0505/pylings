"""
maximum_depth_of_binary_tree — Maximum Depth (NeetCode) difficulty: easy

Given the root of a binary tree, return its maximum depth.
Goal: O(n) time.
"""

# I AM NOT DONE

# Concept Tip: The depth of a node is 1 plus the depth of its deeper child.


class TreeNode:
    def __init__(self, val: int = 0, left: "TreeNode | None" = None, right: "TreeNode | None" = None) -> None:
        self.val = val
        self.left = left
        self.right = right


def max_depth(root: TreeNode | None) -> int:
    # TODO: implement
    raise NotImplementedError


# ---------------------------------------------------------------- tests


def test_max_depth():
    root = TreeNode(3, TreeNode(9), TreeNode(20, TreeNode(15), TreeNode(7)))
    assert max_depth(root) == 3
    assert max_depth(None) == 0
    assert max_depth(TreeNode(1)) == 1
