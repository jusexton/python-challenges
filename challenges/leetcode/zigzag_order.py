from collections import deque
from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def zigzag_level_order(self, root: Optional[TreeNode]) -> list[list[int]]:
    if root is None:
        return []

    levels = []
    queue = deque([root])
    reverse = False
    while queue:
        level_size = len(queue)
        current_level = []

        for _ in range(level_size):
            node = queue.popleft()
            assert node
            current_level.append(node.val)

            if node.left:
                queue.append(node.left)
            if node.right:
                queue.append(node.right)

        levels.append(current_level[::-1] if reverse else current_level)
        reverse = not reverse

    return levels
