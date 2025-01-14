from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


def delete_middle(head: Optional[ListNode]) -> Optional[ListNode]:
    slow, fast = head, head.next.next  # type: ignore
    while fast and fast.next:
        fast = fast.next.next
        slow = slow.next  # type: ignore
    slow.next = slow.next.next  # type: ignore
    return head
