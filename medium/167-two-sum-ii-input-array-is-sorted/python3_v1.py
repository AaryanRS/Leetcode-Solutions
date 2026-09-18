# Pushed: 2026-09-18 12:12:14 UTC
# Difficulty: Medium
# Runtime: 4 ms
# Memory: 22.6 MB

class Solution:
    def twoSum(self, numbers: list[int], target: int) -> list[int]:
        low = 0
        high = len(numbers)-1

        while low < high:
            if numbers[low] + numbers[high] == target:
                return [low+1, high+1]
            elif numbers[low] + numbers[high] < target:
                low += 1
            else:
                high -= 1
        return [-1,-1]