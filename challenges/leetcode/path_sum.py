from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def has_path_sum(root: Optional[TreeNode], target_sum: int) -> bool:
    def inner(node: Optional[TreeNode], current_sum: int):
        if not node:
            return False

        current_sum += node.val
        if not node.left and not node.right:
            return current_sum == target_sum
        return inner(node.left, current_sum) or inner(node.right, current_sum)

    return inner(root, 0)
