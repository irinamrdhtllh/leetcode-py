# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        self.n_good = 0
        self.traverse(root, root.val)
        return self.n_good

    def traverse(self, node: TreeNode, max_so_far: int):
        if node is None:
            return
        if node.val >= max_so_far:
            self.n_good += 1
        max_so_far = max(max_so_far, node.val)
        self.traverse(node.left, max_so_far)
        self.traverse(node.right, max_so_far)
