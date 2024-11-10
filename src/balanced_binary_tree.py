from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    balanced = True

    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        self.traverse(root)
        return self.balanced

    def traverse(self, node: Optional[TreeNode]):
        if node is None:
            return -1
        height_l = self.traverse(node.left)
        height_r = self.traverse(node.right)
        height = max(height_l, height_r) + 1
        if abs(height_l - height_r) > 1:
            self.balanced = False
        return height
