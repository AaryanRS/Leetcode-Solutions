# Pushed: 2026-10-16 10:07:04 UTC
# Difficulty: Medium
# Runtime: 0 ms
# Memory: 19.3 MB

class Solution:
    def trailingZeroes(self, n: int) -> int:
        count = 0
        divisor = 5 

        while n >= divisor:
            count += n //divisor
            divisor *= 5 
        
        return count

        