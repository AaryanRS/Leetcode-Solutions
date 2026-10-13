# Pushed: 2026-10-13 05:10:22 UTC
# Difficulty: Easy
# Runtime: 13 ms
# Memory: 23.5 MB

class Solution:
    def isPalindrome(self, s: str) -> bool:
        s = ''.join(c.lower() for c in s if c.isalnum())
        left = 0 
        right = len(s) - 1

        while left < right:
            if s[left] != s[right]:
                return False
            left += 1
            right -= 1
        
        return True
        
