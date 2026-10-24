# Pushed: 2026-10-24 09:25:37 UTC
# Difficulty: Easy
# Runtime: 0 ms
# Memory: 18.9 MB

class Solution:
    def findTheDifference(self, s: str, t: str) -> str:
        for c in t:
            if t.count(c) > s.count(c):
                return(c)