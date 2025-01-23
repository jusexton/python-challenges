class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def good_nodes(root: TreeNode) -> int:
    good_count = 0
    stack = [(root, root.val)]
    while stack:
        node, max_val = stack.pop()
        if node.val >= max_val:
            good_count += 1

        new_max = max(node.val, max_val)
        if node.left:
            stack.append((node.left, new_max))
        if node.right:
            stack.append((node.right, new_max))

    return good_count
