from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None) -> None:
        self.val = 0
        self.left = None
        self.right = None


def reverse_tree(root: Optional[TreeNode]):
    if not root:
        return
    root.left, root.right = root.right, root.left
    reverse_tree(root.left)
    reverse_tree(root.right)
