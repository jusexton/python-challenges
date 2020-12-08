from collections import deque
from typing import Dict


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def max_level_sum(root: TreeNode) -> int:
    sums = tree_level_sums(root)

    max_level, max_sum = 0, float('-inf')
    for level, summation in sums.items():
        if summation > max_sum:
            max_level = level
            max_sum = summation

    return max_level


def tree_level_sums(root: TreeNode) -> Dict[int, int]:
    level = 1
    level_sums = {}
    queue = deque([root])

    while queue:
        next_level = deque()
        level_sum = 0
        for node in queue:
            level_sum += node.val
            if node.left:
                next_level.append(node.left)
            if node.right:
                next_level.append(node.right)

        level_sums[level] = level_sum
        level += 1
        queue = next_level

    return level_sums
