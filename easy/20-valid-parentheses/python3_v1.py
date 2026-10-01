# Pushed: 2026-10-01 03:53:26 UTC
# Difficulty: Easy
# Runtime: 0 ms
# Memory: 19.3 MB

class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        for ch in s:
            if ch in "({[":
                stack.append(ch)
            else:
                if not stack:
                    return False
                top = stack.pop()
                if ch == ")" and top != "(":
                    return False 
                if ch == "}" and top != "{":
                    return False 
                if ch == "]" and top != "[":
                    return False 
        return not stack