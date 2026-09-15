# Pushed: 2026-09-15 06:26:37 UTC
# Difficulty: Easy
# Runtime: 4 ms
# Memory: 19.2 MB

class Solution:
    def mySqrt(self, x: int) -> int:
        low = 0
        high = x//2
        ans = 0

        if x < 2:
            return x

        while low <= high:
            mid = (low+high)//2

            if mid*mid == x:
                return mid
            elif mid*mid < x:
                ans = mid
                low = mid+1
            else:
                high = mid-1
        return ans