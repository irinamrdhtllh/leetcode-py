from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        return self.traverse(p, q)

    def traverse(self, node1: Optional[TreeNode], node2: Optional[TreeNode]):
        if node1 is None or node2 is None:
            if node1 == node2:
                return True
            return False

        if node1.val != node2.val:
            return False

        if self.traverse(node1.left, node2.left) is False:
            return False

        if self.traverse(node1.right, node2.right) is False:
            return False

        return True
