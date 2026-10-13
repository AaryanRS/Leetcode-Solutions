# Pushed: 2026-10-13 05:33:00 UTC
# Difficulty: Easy
# Runtime: 0 ms
# Memory: 21.1 MB

class Solution:
    def singleNumber(self, nums: list[int]) -> int:
        res = 0

        for i in nums:
            res ^= i
        
        return res