# Pushed: 2026-10-16 10:36:33 UTC
# Difficulty: Easy
# Runtime: 2 ms
# Memory: 19.3 MB

class Solution:
    def reverseBits(self, n: int) -> int:
        res = 0
        for i in range(32):
            res = (res << 1) | (n & 1)
            n >>= 1
        return res