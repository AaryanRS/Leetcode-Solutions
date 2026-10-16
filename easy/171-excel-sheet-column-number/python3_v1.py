# Pushed: 2026-10-16 10:00:52 UTC
# Difficulty: Easy
# Runtime: 0 ms
# Memory: 19 MB

class Solution:
    def titleToNumber(self, columnTitle: str) -> int:
        ans = 0

        for ch in columnTitle:
            ans = ans * 26 + (ord(ch) - ord("A") + 1)
        return ans