# Pushed: 2026-10-24 09:23:59 UTC
# Difficulty: Easy
# Runtime: 72 ms
# Memory: 19.4 MB

class Solution:
    def firstUniqChar(self, s: str) -> int:
        freq = {}
        for c in s:
            freq[c] = 1 + freq.get(c, 0)
        
        for i, c in enumerate(s):
            if freq[c] == 1:
                return i
        
        return -1