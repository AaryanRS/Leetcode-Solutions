# Pushed: 2026-10-24 09:26:45 UTC
# Difficulty: Medium
# Runtime: 7 ms
# Memory: 20 MB

class Solution:
    def lastRemaining(self, n: int) -> int:
        def helper(x, step, count, direction):
            if count < 2:
                return x
            increment = step if direction or count % 2 else 0
            return helper(x + increment, step * 2, count // 2, not direction)

        return helper(1, 1, n, True)