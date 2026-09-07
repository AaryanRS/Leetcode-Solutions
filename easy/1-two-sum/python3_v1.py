# Pushed: 2026-09-07 13:37:52 UTC
# Difficulty: Easy
# Runtime: 3 ms
# Memory: 20.5 MB

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
            freq_map = {}

            for i in range(len(nums)):
                remaining = target - nums[i]
                if remaining in freq_map:
                    return [freq_map[remaining], i]
                freq_map[nums[i]] = i