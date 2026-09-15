# Pushed: 2026-09-15 05:02:45 UTC
# Difficulty: Medium
# Runtime: 0 ms
# Memory: 19.5 MB

class Solution:
    def search(self, nums: List[int], target: int) -> int:

        index = -1 
        low = 0
        high = len(nums) - 1

        while low <= high:
            mid = (low+high)//2
            if target == nums[mid]:
                index = mid
                return mid
            if nums[mid] <= nums[high]:
                if nums[mid] <= target <= nums[high]:
                    low = mid+1
                else:
                    high = mid-1
            else:
                if nums[low] <= target <= nums[mid]:
                    high = mid-1
                else:
                    low = mid+1
        return index