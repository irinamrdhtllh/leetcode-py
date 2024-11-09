from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


def reverseList(head: Optional[ListNode]) -> Optional[ListNode]:
    node = head
    new_head = None
    while node:
        next_node = node.next
        node.next = new_head
        new_head = node
        node = next_node
    return new_head
