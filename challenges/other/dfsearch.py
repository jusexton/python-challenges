from collections import deque


class TreeNode:
    def __init__(self, data: int, nodes: list = None):
        self.data = data
        self.nodes = nodes or []


def search(tree: TreeNode) -> list[int]:
    if tree is None:
        return []
    visited, stack = [], deque([tree])
    while stack:
        node = stack.pop()
        visited.append(node.data)
        stack.extend(node.nodes[::-1])
    return visited
