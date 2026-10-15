# Pushed: 2026-10-15 05:27:34 UTC
# Difficulty: Medium
# Runtime: 4 ms
# Memory: 19.8 MB

class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        res = max(nums)
        cur_max = cur_min = 1

        for n in nums:
            temp = cur_max * n
            cur_max = max(temp, cur_min * n, n)
            cur_min = min(temp, cur_min * n, n)

            res = max(res, cur_max)
        
        return res
        