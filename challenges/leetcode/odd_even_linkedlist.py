from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


def odd_even_list(self, head: Optional[ListNode]) -> Optional[ListNode]:
    if head is None or head.next is None:
        return head

    odd = head
    even = head.next
    even_head = head.next

    while even and even.next:
        odd.next = odd.next.next  # type: ignore
        even.next = even.next.next
        odd = odd.next
        even = even.next
    odd.next = even_head

    return head
