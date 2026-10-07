# Pushed: 2026-10-07 05:25:08 UTC
# Difficulty: Easy
# Runtime: 3 ms
# Memory: 19.2 MB

class Solution:
    def isPalindrome(self, x: int) -> bool:
        a= x
        if x < 0:
            return False
        total = 0
        while a != 0:
            b = a % 10
            total = total * 10 + b
            a //= 10 
        if x == total:
            return True
        else:
            return False