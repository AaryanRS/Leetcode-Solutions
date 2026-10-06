# Pushed: 2026-10-06 00:45:46 UTC
# Difficulty: Easy
# Runtime: 46 ms
# Memory: 36.2 MB

class Solution:
    def containsNearbyDuplicate(self, nums: list[int], k: int) -> bool:
        windows_set = set()

        for i in range(len(nums)):
            if i > k:
                windows_set.remove(nums[i-k-1])
            if nums[i] in windows_set:
                return True
            windows_set.add(nums[i])

        return False