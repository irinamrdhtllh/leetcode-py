from typing import Optional


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def leafSimilar(root1: Optional[TreeNode], root2: Optional[TreeNode]) -> bool:
    leaves1 = []
    leaves2 = []
    traverse(root1, leaves1)
    traverse(root2, leaves2)
    return leaves1 == leaves2


def traverse(node, leaves):
    if node is None:
        return
    if node.left is None and node.right is None:
        leaves.append(node.val)
        return
    traverse(node.left, leaves)
    traverse(node.right, leaves)
