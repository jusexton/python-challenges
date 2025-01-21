from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


def odd_even_list(self, head: Optional[ListNode]) -> Optional[ListNode]:
    if head is None or head.next is None:
        return head

    curr_odd = head
    curr_even = head.next
    even_head = head.next

    while curr_even and curr_even.next:
        curr_odd.next = curr_odd.next.next  # type: ignore
        curr_even.next = curr_even.next.next
        curr_odd = curr_odd.next
        curr_even = curr_even.next
    curr_odd.next = even_head

    return head
