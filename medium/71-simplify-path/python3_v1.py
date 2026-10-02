# Pushed: 2026-10-02 04:46:52 UTC
# Difficulty: Medium
# Runtime: 4 ms
# Memory: 19.3 MB

class Solution:
    def simplifyPath(self, path: str) -> str:
        s = path.split("/")
        res = []
        
        for i in s:
            if i == ".." and res:
                res.pop()
            elif i == "." or i == "" or i == "..":
                continue
            else:
                res.append(i)
        
        return "/" + "/".join(res)