# Pushed: 2026-10-02 04:17:38 UTC
# Difficulty: Hard
# Runtime: 3 ms
# Memory: 19.4 MB

class Solution:
    def isNumber(self, s: str) -> bool:
        hash_dict = {"+": 0, "-": 0, ".": 0, "e": 0}
        seen_digit = False 
        
        for i in range(len(s)):
            char = s[i]
            
            if char in ("-", "+"):
                if i > 0 and s[i-1] not in ("e", "E"):
                    return False
                if hash_dict[char] >= 1:
                    return False
                hash_dict[char] += 1
                
            elif char == ".":
                if hash_dict["e"] > 0 or hash_dict["."] >= 1:
                    return False
                hash_dict["."] += 1
                
            elif char in ("e", "E"):
                if not seen_digit or hash_dict["e"] >= 1:
                    return False
                hash_dict["e"] += 1
                seen_digit = False
                hash_dict["+"] = 0
                hash_dict["-"] = 0 
                
            elif char.isdigit():
                seen_digit = True
                
            else:
                return False 
                
        return seen_digit
