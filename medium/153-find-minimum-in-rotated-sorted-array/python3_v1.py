# Pushed: 2026-09-18 11:06:00 UTC
# Difficulty: Medium
# Runtime: 0 ms
# Memory: 19.4 MB

class Solution:
    def findMin(self, nums: list[int]) -> int:
        low = 0
        high = len(nums) - 1
        
        while low < high:
            mid = (low+high)//2
            if nums[mid] > nums[high]:
                low = mid + 1
            else:
                high = mid
        return nums[low]