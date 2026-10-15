# Pushed: 2026-10-15 05:04:51 UTC
# Difficulty: Medium
# Runtime: 4 ms
# Memory: 20.6 MB

class Solution:
    def singleNumber(self, nums: list[int]) -> int:
        ones = 0
        twos = 0
        for num in nums:
            twos ^= (ones & num)
            ones ^= num
            threes = ones & twos
            ones &= ~threes
            twos &= ~threes
            
        return ones