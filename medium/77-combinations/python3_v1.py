# Pushed: 2026-10-11 06:42:50 UTC
# Difficulty: Medium
# Runtime: 119 ms
# Memory: 61.3 MB

class Solution:
    def combine(self, n: int, k: int) -> list[list[int]]:
        res = []
        def combinations(start, subarray):
            if len(subarray) == k:
                res.append(subarray.copy())
                return 
            if start > n:
                return
            subarray.append(start)
            combinations(start+1, subarray)
            subarray.pop()
            combinations(start+1, subarray) 
        combinations(1, [])
        return res

                