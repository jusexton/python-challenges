# https://leetcode.com/problems/invert-binary-tree
# Tags: Tree, Binary Tree

from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def invert_tree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
    stack = [root] if root else []
    while stack:
        node = stack.pop()
        assert node

        temp = node.left
        node.left = node.right
        node.right = temp

        if node.left:
            stack.append(node.left)
        if node.right:
            stack.append(node.right)

    return root
