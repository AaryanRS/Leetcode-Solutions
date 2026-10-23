# Pushed: 2026-10-23 07:22:40 UTC
# Difficulty: Easy
# Runtime: 3 ms
# Memory: 20.4 MB

class Solution:
    def moveZeroes(self, nums: list[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        left = 0

        for right in range(len(nums)):
            if nums[right] != 0:
                nums[right], nums[left] = nums[left], nums[right]
                left += 1
        
        return nums
        