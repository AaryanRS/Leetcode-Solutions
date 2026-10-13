# Pushed: 2026-10-13 05:26:52 UTC
# Difficulty: Medium
# Runtime: 55 ms
# Memory: 36.6 MB

class Solution:
    def longestConsecutive(self, nums: list[int]) -> int:
        num_set = set(nums)
        longest = 0
        
        for num in num_set:
            if (num - 1) not in num_set:
                current_num = num
                current_streak = 1
                
                while (current_num + 1) in num_set:
                    current_num += 1
                    current_streak += 1
                    
                longest = max(longest, current_streak)
                
        return longest
        