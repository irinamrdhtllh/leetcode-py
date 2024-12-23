from typing import Optional


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


def deleteMiddle(head: Optional[ListNode]) -> Optional[ListNode]:
    if not head or not head.next:
        return None

    node = head
    nodes = []
    while node:
        nodes.append(node)
        node = node.next

    mid = len(nodes) // 2

    if mid == 0:
        return None
    else:
        prev_node = nodes[mid - 1]
        prev_node.next = nodes[mid].next

    return head
