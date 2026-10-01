# Pushed: 2026-10-01 04:36:00 UTC
# Difficulty: Easy
# Runtime: 0 ms
# Memory: 19.4 MB

class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        for i in range(len(haystack)-len(needle)+1):
            if haystack[i:i+len(needle)] == needle:
                return i 
        return -1