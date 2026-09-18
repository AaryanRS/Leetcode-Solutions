# Pushed: 2026-09-18 11:37:18 UTC
# Difficulty: Medium
# Runtime: 0 ms
# Memory: 19.4 MB

class Solution:
    def findPeakElement(self, nums: list[int]) -> int:
        low = 0
        high = len(nums) - 1
        while low < high:
            mid = (low + high)//2
            if nums[mid] < nums[mid+1]:
                low = mid + 1 
            else:
                high = mid
        return low