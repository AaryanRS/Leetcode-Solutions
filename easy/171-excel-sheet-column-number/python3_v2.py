# Pushed: 2026-10-16 10:02:08 UTC
# Difficulty: Easy
# Runtime: 1 ms
# Memory: 19.1 MB

class Solution:
    def titleToNumber(self, columnTitle: str) -> int:
        ans = 0

        for ch in columnTitle:
            ans = ans * 26 + (ord(ch) - ord("A") + 1)
        return ans