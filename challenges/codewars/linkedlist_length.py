from typing import Optional


class Node:
    def __init__(self, data: int, next: Optional["Node"] = None):
        self.data = data
        self.next = next


def length(node: Node | None) -> int:
    result = 0
    while node is not None:
        result += 1
        node = node.next

    return result
