# https://leetcode.com/problems/same-tree
# Tags: Tree, Binary Tree, Depth First Search


from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

    def __repr__(self):
        return f"TreeNode(val={self.val})"


# Recusive approach
# def is_same_tree(p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
#     if p is None and q is None:
#         return True
#     if p is None or q is None or p.val != q.val:
#         return False
#     return is_same_tree(p.left, q.left) and is_same_tree(p.right, q.right)


# Iterative approach
def is_same_tree(p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
    stack = [p, q]
    while stack:
        q_node = stack.pop()
        p_node = stack.pop()

        if q_node is None and p_node is None:
            continue

        if p_node is None or q_node is None or p_node.val != q_node.val:
            return False

        stack.append(p_node.left)
        stack.append(q_node.left)
        stack.append(p_node.right)
        stack.append(q_node.right)

    return True
