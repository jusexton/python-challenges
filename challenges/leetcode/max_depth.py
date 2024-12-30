# https://leetcode.com/problems/maximum-depth-of-binary-tree
# Tags: Tree, Binary Tree, Depth First Search

from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


# Iterative approach
# def max_depth(root: Optional[TreeNode]) -> int:
#     if not root:
#         return 0

#     max_depth = 0
#     stack = [(root, 1)]
#     while stack:
#         node, depth = stack.pop()
#         max_depth = max(max_depth, depth)

#         assert node
#         if node.left:
#             stack.append((node.left, depth + 1))
#         if node.right:
#             stack.append((node.right, depth + 1))

#     return max_depth


# Recrusive approach
def max_depth(root: Optional[TreeNode]) -> int:
    if not root:
        return 0
    return max(1 + max_depth(root.left), 1 + max_depth(root.right))
