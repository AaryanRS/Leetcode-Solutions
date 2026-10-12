# Pushed: 2026-10-12 05:54:48 UTC
# Difficulty: Medium
# Runtime: 4 ms
# Memory: 19.2 MB

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def partition(self, head: ListNode | None, x: int) -> ListNode | None:
        less_head = ListNode(0)
        greater_head = ListNode(0)
        less = less_head
        greater = greater_head

        while head:
            if head.val < x:
                less.next = head
                less = less.next
            else:
                greater.next = head
                greater = greater.next
            head = head.next

        greater.next = None
        less.next = greater_head.next

        return less_head.next