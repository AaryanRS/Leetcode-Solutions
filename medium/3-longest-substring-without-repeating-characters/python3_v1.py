# Pushed: 2026-09-26 04:18:42 UTC
# Difficulty: Medium
# Runtime: 416 ms
# Memory: 19.8 MB

class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        start = 0
        end = 0 
        hash_dict = {}
        max_len = 0
        while end != len(s):
            if s[end] in hash_dict and hash_dict[s[end]] > 0:
                hash_dict[s[start]] -= 1
                start += 1 
            else:
                hash_dict[s[end]] = hash_dict.get(s[end], 0) + 1 
                max_len = max(max_len,(end - start + 1))
                end += 1
        return max_len