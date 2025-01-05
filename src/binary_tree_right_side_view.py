from typing import List, Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        if root is None:
            return []

        queue = [root]
        right_side_nodes = []

        while queue:
            level_size = len(queue)
            for i in range(level_size):
                node = queue.pop(0)
                if i == level_size - 1:
                    right_side_nodes.append(node.val)
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)

        return right_side_nodes
