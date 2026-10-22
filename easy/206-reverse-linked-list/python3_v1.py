# Pushed: 2026-10-22 05:19:15 UTC
# Difficulty: Easy
# Runtime: 0 ms
# Memory: 20.3 MB

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseList(self, head: ListNode | None) -> ListNode | None:
        node = None

        while head:
            temp = head.next
            head.next = node
            node = head
            head = temp
        
        return node