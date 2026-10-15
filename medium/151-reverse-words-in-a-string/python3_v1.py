# Pushed: 2026-10-15 05:20:26 UTC
# Difficulty: Medium
# Runtime: 0 ms
# Memory: 19.3 MB

class Solution:
    def reverseWords(self, s: str) -> str:
        a = s.split()
        return " ".join(a[::-1])