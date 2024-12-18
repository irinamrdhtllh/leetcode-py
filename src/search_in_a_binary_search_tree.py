from typing import Optional


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def searchBST(root: Optional[TreeNode], val: int) -> Optional[TreeNode]:
    return traverse(root, val)


def traverse(node, val):
    if node is None:
        return None
    if val == node.val:
        return node
    if val < node.val:
        return traverse(node.left, val)
    if val > node.val:
        return traverse(node.right, val)
