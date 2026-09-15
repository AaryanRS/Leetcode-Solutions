# Pushed: 2026-09-15 05:54:45 UTC
# Difficulty: Easy
# Runtime: 0 ms
# Memory: 20 MB

class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        index = len(nums)
        low = 0
        high = len(nums)-1

        while low <= high:
            mid = (low+high)//2
            if nums[mid] >= target:
                index = mid
                high = mid-1
            else:
                low = mid+1
        return index