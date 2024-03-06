from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def search(root: TreeNode | None, val: int) -> Optional[TreeNode]:
    while root:
        if val == root.val:
            return root
        elif root.val < val:
            root = root.right
        else:
            root = root.left

    return None
