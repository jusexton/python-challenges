from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


def add_two_numbers(
    self, l1: Optional[ListNode], l2: Optional[ListNode]
) -> Optional[ListNode]:
    dummy_head = ListNode(0)
    tail = dummy_head

    carry = 0
    while l1 or l2 or carry != 0:
        n_one = l1.val if l1 else 0
        n_two = l2.val if l2 else 0

        res = n_one + n_two + carry
        digit = res % 10
        carry = res // 10

        tail.next = ListNode(digit)
        tail = tail.next

        l1 = l1.next if l1 else None
        l2 = l2.next if l2 else None

    return dummy_head.next
