# Pushed: 2026-10-06 01:18:03 UTC
# Difficulty: Easy
# Runtime: 4 ms
# Memory: 20.4 MB

class Solution:
    def missingNumber(self, nums: list[int]) -> int:
        n = len(nums)
        r = n * (n+1) // 2
        for i in nums:
            r -= i
        return r