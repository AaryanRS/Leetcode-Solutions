# Pushed: 2026-10-07 05:44:21 UTC
# Difficulty: Easy
# Runtime: 0 ms
# Memory: 19.3 MB

class Solution:
    def plusOne(self, digits: list[int]) -> list[int]:
        a = (str(i) for i in digits)
        b ="".join(a)
        b = str(int(b) + 1) 
        return [int(char) for char in b]