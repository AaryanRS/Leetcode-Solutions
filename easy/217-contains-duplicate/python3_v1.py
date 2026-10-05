# Pushed: 2026-10-05 16:41:02 UTC
# Difficulty: Easy
# Runtime: 2 ms
# Memory: 32.1 MB

class Solution:
    def containsDuplicate(self, nums: list[int]) -> bool:
        return True if len(set(nums)) < len(nums) else False