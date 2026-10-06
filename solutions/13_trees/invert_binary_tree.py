"""
invert_binary_tree — Solution
"""


class TreeNode:
    def __init__(self, val: int = 0, left: "TreeNode | None" = None, right: "TreeNode | None" = None) -> None:
        self.val = val
        self.left = left
        self.right = right


def invert_tree(root: TreeNode | None) -> TreeNode | None:
    if not root:
        return None
    root.left, root.right = invert_tree(root.right), invert_tree(root.left)
    return root


# ---------------------------------------------------------------- tests


def test_invert():
    root = TreeNode(4, TreeNode(2, TreeNode(1), TreeNode(3)), TreeNode(7, TreeNode(6), TreeNode(9)))
    inv = invert_tree(root)
    assert inv.val == 4
    assert inv.left.val == 7
    assert inv.right.val == 2
    assert inv.left.left.val == 9
