class Node:
    def __init__(self, data: int, next: 'Node' = None):
        self.data = data
        self.next = next


def length(node: Node) -> int:
    result = 0
    while node is not None:
        result += 1
        node = node.next

    return result
