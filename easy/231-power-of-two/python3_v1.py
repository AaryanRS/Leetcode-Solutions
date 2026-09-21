# Pushed: 2026-09-21 12:08:37 UTC
# Difficulty: Easy
# Runtime: 0 ms
# Memory: 19.2 MB

class Solution:
    def isPowerOfTwo(self, n: int) -> bool:
        return n > 0 and (n & (n-1)) == 0