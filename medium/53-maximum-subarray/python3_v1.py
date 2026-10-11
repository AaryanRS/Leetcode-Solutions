# Pushed: 2026-10-11 05:57:23 UTC
# Difficulty: Medium
# Runtime: 35 ms
# Memory: 31.4 MB

class Solution:
    def maxSubArray(self, nums: list[int]) -> int:
        cur_max, max_till_now = 0, -inf
        for c in nums:
            cur_max = max(c, cur_max + c)
            max_till_now = max(max_till_now, cur_max)
        return max_till_now