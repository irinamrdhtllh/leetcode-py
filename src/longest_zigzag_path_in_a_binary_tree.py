from typing import Optional


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def longestZigZag(self, root: Optional[TreeNode]) -> int:
        self.longest_path = 0
        self.traverse(root, "left", 0)
        self.traverse(root, "right", 0)
        return self.longest_path

    def traverse(self, node: Optional[TreeNode], direction: str, path: int):
        if node is None:
            return
        self.longest_path = max(self.longest_path, path)
        if direction == "left":
            self.traverse(node.right, "left", 1)
            self.traverse(node.left, "right", path + 1)
        else:
            self.traverse(node.right, "left", path + 1)
            self.traverse(node.left, "right", 1)
