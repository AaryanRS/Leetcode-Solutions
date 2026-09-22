# Pushed: 2026-09-22 00:49:01 UTC
# Difficulty: Medium
# Runtime: 0 ms
# Memory: 19.1 MB

class Solution:
    def reverse(self, x: int) -> int:
        result = 0
        y = abs(x)
        while y != 0:
            digit = y % 10
            result = result*10 + digit
            y = y // 10
        if x < 0:
            result =  -result

        Min_int = -2**31
        Max_int = 2**31 - 1

        if Min_int > result or result > Max_int:
            return 0
        
        return result