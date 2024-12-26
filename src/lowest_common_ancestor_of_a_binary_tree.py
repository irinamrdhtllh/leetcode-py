# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def lowestCommonAncestor(
        self, root: TreeNode, p: TreeNode, q: TreeNode
    ) -> TreeNode:
        self.p = p
        self.q = q
        self.LCA = self.traverse(root)
        return self.LCA

    def traverse(self, node: TreeNode) -> TreeNode:
        if node is None:
            return None
        if node == self.p or node == self.q:
            return node
        left_node = self.traverse(node.left)
        right_node = self.traverse(node.right)
        if left_node and right_node:
            return node
        elif left_node:
            return left_node
        elif right_node:
            return right_node
