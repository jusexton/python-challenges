from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


def remove_nth_from_end(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
    fast, slow = head, head

    # Move fast in front so that the gap between slow and fast becomes n
    # Later, we will move fast to the end and based on the gap of slow
    # we'll know what to delete,
    for _ in range(n):
        fast = fast.next  # type: ignore

    # When fast pointer builds a gap so large that it does not point to a node
    # this means to delete the first node, thus, we simply return the next node after head.
    if not fast:
        return head.next  # type: ignore

    # Move fast to the end, maintaining the gap
    while fast.next:  # type: ignore
        fast, slow = fast.next, slow.next  # type: ignore

    # Skip the node at the gap
    slow.next = slow.next.next  # type: ignore
    return head
