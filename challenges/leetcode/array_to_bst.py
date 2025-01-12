from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def sorted_array_to_bst(numbers: list[int]) -> Optional[TreeNode]:
    if not numbers:
        return None

    mid = len(numbers) // 2
    root = TreeNode(numbers[mid])
    root.left = sorted_array_to_bst(numbers[:mid])
    root.right = sorted_array_to_bst(numbers[mid + 1 :])
    return root
