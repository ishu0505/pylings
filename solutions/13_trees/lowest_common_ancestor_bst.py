"""
lowest_common_ancestor_bst — Solution
"""


class TreeNode:
    def __init__(self, val: int = 0, left: "TreeNode | None" = None, right: "TreeNode | None" = None) -> None:
        self.val = val
        self.left = left
        self.right = right


def lowest_common_ancestor(root: TreeNode, p: TreeNode, q: TreeNode) -> TreeNode:
    curr = root
    while curr:
        if p.val < curr.val and q.val < curr.val:
            assert curr.left is not None
            curr = curr.left
        elif p.val > curr.val and q.val > curr.val:
            assert curr.right is not None
            curr = curr.right
        else:
            return curr
    return root


# ---------------------------------------------------------------- tests


def test_lca_bst():
    p = TreeNode(2)
    q = TreeNode(8)
    root = TreeNode(6, p, q)
    assert lowest_common_ancestor(root, p, q).val == 6
