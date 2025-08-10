from typing import Optional


class Node:
    def __init__(self, data: int, next: Optional["Node"] = None):
        self.data = data
        self.next = next


def count(node: Node | None, data: int) -> int:
    result = 0
    while node is not None:
        if node.data == data:
            result += 1

        node = node.next

    return result
