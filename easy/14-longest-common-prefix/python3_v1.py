# Pushed: 2026-09-15 04:42:42 UTC
# Difficulty: Easy
# Runtime: 0 ms
# Memory: 19.2 MB

class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
            shortest = min(strs, key=len)
            output = ""
            for i in range(len(shortest)):
                for word in strs:
                    if word[i] != shortest[i]:
                        return shortest[:i]        
            return shortest