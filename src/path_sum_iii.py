from typing import Optional


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def pathSum(self, root: Optional[TreeNode], targetSum: int) -> int:
        self.target = targetSum
        self.n_path = 0
        self.traverse(root, [])
        return self.n_path

    def traverse(self, node, path):
        if node is None:
            return
        path.append(node)
        sum = 0
        for i in range(len(path) - 1, -1, -1):
            sum += path[i].val
            if sum == self.target:
                self.n_path += 1
        self.traverse(node.left, path)
        self.traverse(node.right, path)
        path.pop()
