# Pushed: 2026-10-12 06:21:05 UTC
# Difficulty: Easy
# Runtime: 46 ms
# Memory: 28.6 MB

class Solution:
    def maxProfit(self, prices: list[int]) -> int:
        maxnumb = 0
        minnumb = float("inf")
        for i in range(len(prices)):
            if prices[i] < minnumb:
                minnumb = prices[i]
            else:
                maxnumb = max(maxnumb, prices[i] - minnumb)
        
        return maxnumb

