from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def leaf_sequence(head: Optional[TreeNode]) -> list[int]:
    sequence = []
    stack = [head]
    while stack:
        curr = stack.pop()

        assert curr
        if curr.left is None and curr.right is None:
            sequence.append(curr.val)

        if curr.right:
            stack.append(curr.right)
        if curr.left:
            stack.append(curr.left)

    return sequence


def leaf_similar(self, root1: Optional[TreeNode], root2: Optional[TreeNode]) -> bool:
    return leaf_sequence(root1) == leaf_sequence(root2)
