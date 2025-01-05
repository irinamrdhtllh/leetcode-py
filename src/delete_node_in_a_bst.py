from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def deleteNode(self, root: Optional[TreeNode], key: int) -> Optional[TreeNode]:
        node = root

        if node is None:
            return

        if key < node.val:
            node.left = self.deleteNode(node.left, key)
        elif key > node.val:
            node.right = self.deleteNode(node.right, key)
        else:
            if node.left is None and node.right is None:
                return None
            elif node.left is None:
                return node.right
            elif node.right is None:
                return node.left
            elif node.left and node.right:
                successor = self.findSuccessor(node.right)
                node.val = successor.val
                node.right = self.deleteNode(node.right, successor.val)

        return node

    def findSuccessor(self, node: Optional[TreeNode]) -> Optional[TreeNode]:
        while node.left:
            node = node.left
        return node
