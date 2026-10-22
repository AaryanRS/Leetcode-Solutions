# Pushed: 2026-10-22 05:23:44 UTC
# Difficulty: Medium
# Runtime: 55 ms
# Memory: 31 MB

class Solution:
    def findKthLargest(self, nums: list[int], k: int) -> int:
        return sorted(nums, reverse=True)[k-1]