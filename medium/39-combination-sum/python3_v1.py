# Pushed: 2026-09-29 04:10:15 UTC
# Difficulty: Medium
# Runtime: 12 ms
# Memory: 19.6 MB

class Solution:
    def combinationSum(self, candidates: list[int], target: int) -> list[list[int]]:
        res = []
        
        def make_combination(idx, comb, total):
            if total == target:
                res.append(comb[:])
                return
            
            if total > target or idx >= len(candidates):
                return
            
            comb.append(candidates[idx])
            make_combination(idx, comb, total + candidates[idx])
            comb.pop()
            make_combination(idx+1, comb, total)

            return res
        
        return make_combination(0, [], 0)
        