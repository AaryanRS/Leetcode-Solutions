# Pushed: 2026-09-29 04:44:15 UTC
# Difficulty: Medium
# Runtime: 19 ms
# Memory: 19.5 MB

class Solution:
    def combinationSum2(self, candidates: list[int], target: int) -> list[list[int]]:
        res = []
        candidates.sort()
        def combination(index, temp, total):
            if total <= 0 or index >= len(candidates):
                if total == 0:
                    res.append(temp.copy())
                return
            for i in range(index, len(candidates)):
                if i > index and candidates[i] == candidates[i-1]:
                    continue
                temp.append(candidates[i])
                combination(i+1, temp, total - candidates[i])
                temp.pop()

            return res
        
        return combination(0, [], target)