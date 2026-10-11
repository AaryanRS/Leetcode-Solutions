# Pushed: 2026-10-11 06:18:28 UTC
# Difficulty: Medium
# Runtime: 0 ms
# Memory: 19.4 MB

class Solution:
    def subsets(self, nums: list[int]) -> list[list[int]]:
        res = []
        def array_subset(start, subarray):
            if start >= len(nums):
                res.append(subarray.copy())
                return 
            subarray.append(nums[start])
            array_subset(start+1, subarray)
            subarray.pop()
            array_subset(start+1, subarray)
            return res 
        return array_subset(0, [])