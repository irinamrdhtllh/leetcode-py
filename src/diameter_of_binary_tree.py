from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    max_diameter = 0

    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        self.traverse(root)
        return self.max_diameter

    def traverse(self, node):
        if node is None:
            return -1

        height_l = self.traverse(node.left)
        height_r = self.traverse(node.right)

        diameter = height_l + height_r + 2

        if diameter > self.max_diameter:
            self.max_diameter = diameter

        return max(height_l, height_r) + 1
