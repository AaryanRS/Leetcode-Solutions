# Pushed: 2026-10-16 09:56:31 UTC
# Difficulty: Easy
# Runtime: 0 ms
# Memory: 19.3 MB

class Solution:
    def convertToTitle(self, columnNumber: int) -> str:
        res = ""

        while columnNumber > 0:
            columnNumber -= 1
            res = chr((columnNumber % 26) + ord("A")) + res
            columnNumber //= 26
        
        return res