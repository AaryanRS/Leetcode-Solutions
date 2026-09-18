# Pushed: 2026-09-18 11:22:03 UTC
# Difficulty: Hard
# Runtime: 0 ms
# Memory: 19.5 MB

class Solution:
    def findMin(self, nums: list[int]) -> int:
        low = 0
        high = len(nums) - 1
        
        while low < high:
            mid = (low+high)//2
            if nums[low] == nums[mid] == nums[high]:
                low +=1
                high -= 1
            elif nums[mid] > nums[high]:
                low = mid + 1
            else:
                high = mid
        return nums[low]