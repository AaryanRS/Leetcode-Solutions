# Pushed: 2026-11-10 16:11:57 UTC
# Difficulty: Medium
# Runtime: 0 ms
# Memory: 19.3 MB

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def swapPairs(self, head: ListNode | None) -> ListNode | None:
        dummy = ListNode(0, head)
        prev, cur = dummy, head

        while cur and cur.next:
            npn = cur.next.next
            second = cur.next

            second.next = cur
            cur.next = npn
            prev.next = second

            prev = cur
            cur = npn
        
        return dummy.next