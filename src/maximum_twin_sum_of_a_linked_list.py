from typing import Optional


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


def pairSum(head: Optional[ListNode]) -> int:
    # Find the middle node
    slow = head
    fast = head
    while fast and fast.next:
        slow = slow.next
        fast = fast.next.next
    mid_node = slow

    # Reverse the second half of the linked-list
    rev_head = None
    curr_node = mid_node
    while curr_node:
        next_node = curr_node.next
        curr_node.next = rev_head
        rev_head = curr_node
        curr_node = next_node

    # Seach for the maximum twin sum
    max_sum = 0
    first = head
    second = rev_head
    while second:
        sum_val = first.val + second.val
        max_sum = max(max_sum, sum_val)
        first = first.next
        second = second.next

    return max_sum
