# Pushed: 2026-10-04 04:52:11 UTC
# Difficulty: Easy
# Runtime: 5 ms
# Memory: 21.6 MB

class Solution:
    def majorityElement(self, nums: list[int]) -> int:
        max_count = 0
        count = 0
        for i in nums:
            if count == 0:
                max_count = i
            if i == max_count:
                count += 1
            else:
                count -= 1 
        return max_count
