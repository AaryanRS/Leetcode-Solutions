# Pushed: 2026-10-01 04:13:51 UTC
# Difficulty: Medium
# Runtime: 3 ms
# Memory: 19.3 MB

class Solution:
    def generateParenthesis(self, n: int) -> list[str]:
        result = []
        subarray = [""] * (2*n)

        def parenthesis(index, subarray, total):
            if index >= len(subarray):
                if total == 0:
                    result.append("".join(subarray))
                return
            if total > len(subarray)//2:
                return
            elif total < 0:
                return 
            subarray[index] = "("
            parenthesis(index+1,subarray,total+1)
            subarray[index] = ")"
            parenthesis(index+1,subarray,total-1)

            return result
        return parenthesis(0, subarray, 0)