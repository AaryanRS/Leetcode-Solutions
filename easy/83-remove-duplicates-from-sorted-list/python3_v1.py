# Pushed: 2026-10-09 04:58:42 UTC
# Difficulty: Easy
# Runtime: 1 ms
# Memory: 19.2 MB

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteDuplicates(self, head: ListNode | None) -> ListNode | None:
        if head is None:
            return None
        
        temp = head

        while temp.next is not None:
            if temp.val == temp.next.val:
                temp.next = temp.next.next
            else:
                temp = temp.next
        return head

