# Pushed: 2026-11-16 08:20:12 UTC
# Difficulty: Medium
# Runtime: 13 ms
# Memory: 20.4 MB

class Solution:
    def canJump(self, nums: list[int]) -> bool:
        goal = len(nums) - 1

        for i in range(len(nums) - 2, -1, -1):
            if i + nums[i] >= goal:
                goal = i
        
        return True if goal == 0 else False