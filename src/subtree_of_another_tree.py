from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        return self.traverse(root, subRoot)

    def traverse(self, node: Optional[TreeNode], subNode: Optional[TreeNode]):
        if node is None:
            return False

        me = self.isSameTree(node, subNode)
        if me:
            return True

        left = self.traverse(node.left, subNode)
        if left:
            return True

        right = self.traverse(node.right, subNode)
        if right:
            return True

        return False

    def isSameTree(self, node1, node2):
        if node1 is None or node2 is None:
            if node1 is None and node2 is None:
                return True
            else:
                return False

        if node1.val != node2.val:
            return False

        left = self.isSameTree(node1.left, node2.left)
        right = self.isSameTree(node1.right, node2.right)

        return left and right
