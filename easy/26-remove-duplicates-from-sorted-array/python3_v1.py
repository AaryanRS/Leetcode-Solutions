# Pushed: 2026-09-28 03:50:42 UTC
# Difficulty: Easy
# Runtime: 4 ms
# Memory: 20.7 MB

class Solution:
    def removeDuplicates(self, nums: list[int]) -> int:
        if not nums:
            return 0
        
        write_index = 1
    
        for i in range(1, len(nums)):
            if nums[i] != nums[i - 1]:
                nums[write_index] = nums[i]
                write_index += 1
                
        return write_index