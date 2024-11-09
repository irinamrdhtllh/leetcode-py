from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    max_depth = 0

    def maxDepth(self, root: Optional[TreeNode]) -> int:
        self.traverse(root)
        return self.max_depth

    def traverse(self, node, depth=1):
        if node is None:
            return
        if depth > self.max_depth:
            self.max_depth = depth
        self.traverse(node.left, depth + 1)
        self.traverse(node.right, depth + 1)
