# Pushed: 2026-09-15 05:29:45 UTC
# Difficulty: Medium
# Runtime: 0 ms
# Memory: 20.7 MB

class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        start = -1
        low = 0
        high = len(nums)-1
        while low <= high:
            mid = (low+high)//2
            if target <= nums[mid]:
                if nums[mid] == target:
                    start = mid
                high = mid-1
            else:
                low = mid+1 

        low = 0
        high = len(nums)-1
        end = -1 
        while low <= high:
            mid = (low+high)//2
            if target < nums[mid]:
                high = mid-1
            else:
                if nums[mid] == target:
                    end = mid
                low = mid+1 

        return [start,end]