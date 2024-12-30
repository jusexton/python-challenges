# https://leetcode.com/problems/merge-two-sorted-lists
# Tags: Linked List

from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


def merge_two_lists(
    self, l1: Optional[ListNode], l2: Optional[ListNode]
) -> Optional[ListNode]:
    dummy_head = ListNode()
    tail = dummy_head
    while l1 and l2:
        if l1.val < l2.val:
            tail.next = l1
            l1, tail = l1.next, l1
        else:
            tail.next = l2
            l2, tail = l2.next, l2

    if l1 or l2:
        tail.next = l1 if l1 else l2

    return dummy_head.next
