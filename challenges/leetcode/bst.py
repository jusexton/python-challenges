class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def binary_search(root: TreeNode | None, val: int):
    if root and root.val > val:
        return binary_search(root.left, val)
    elif root and root.val < val:
        return binary_search(root.right, val)
    else:
        return root
