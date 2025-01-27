class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def inorder(root: TreeNode | None) -> list[int]:
    return inorder(root.left) + [root.val] + inorder(root.right) if root else []
