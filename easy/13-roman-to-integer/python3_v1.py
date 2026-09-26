# Pushed: 2026-09-26 05:04:17 UTC
# Difficulty: Easy
# Runtime: 0 ms
# Memory: 19.1 MB

class Solution:
    def romanToInt(self, s: str) -> int:
        hash_dict = {
            "I" : 1,
            "V" : 5,
            "X" : 10,
            "L" : 50,
            "C" : 100,
            "D" : 500,
            "M" : 1000,
        }

        result = 0 
        for i in range(len(s)):
            if i < len(s) - 1 and hash_dict[s[i]] < hash_dict[s[i+1]]:
                result -= hash_dict[s[i]]
            else:
                result += hash_dict[s[i]]
        return result