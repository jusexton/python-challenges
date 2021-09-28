from collections import deque


class TreeNode:
    def __init__(self, data: int, left=None, right=None):
        self.data = data
        self.left = left
        self.right = right


def search(tree: TreeNode) -> list[int]:
    if tree is None:
        return []
    visited, queue = [], deque([tree])
    while queue:
        node = queue.popleft()
        visited.append(node.data)
        queue.extend(filter(None, [node.left, node.right]))

    return visited
