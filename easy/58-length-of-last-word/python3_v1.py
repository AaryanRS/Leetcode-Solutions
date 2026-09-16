# Pushed: 2026-09-16 17:15:40 UTC
# Difficulty: Easy
# Runtime: 0 ms
# Memory: 19.4 MB

class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        List = s.strip().split()
        return len(List[-1])