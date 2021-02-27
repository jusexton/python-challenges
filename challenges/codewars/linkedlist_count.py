class Node:
    def __init__(self, data: int, next: 'Node' = None):
        self.data = data
        self.next = next


def count(node: Node, data: int) -> int:
    result = 0
    while node is not None:
        if node.data == data:
            result += 1

        node = node.next

    return result
