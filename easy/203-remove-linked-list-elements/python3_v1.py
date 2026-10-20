# Pushed: 2026-10-20 13:17:41 UTC
# Difficulty: Easy
# Runtime: 4 ms
# Memory: 22.4 MB

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeElements(self, head: ListNode | None, val: int) -> ListNode | None:
        dummy = ListNode(0, head)
        temp = dummy
        
        while temp.next is not None:
            if temp.next.val == val:
                temp.next = temp.next.next
            else:
                temp=temp.next
        
        return dummy.next
