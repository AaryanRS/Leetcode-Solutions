# Pushed: 2026-09-27 05:38:40 UTC
# Difficulty: Medium
# Runtime: 527 ms
# Memory: 19.3 MB

class Solution:
    def threeSumClosest(self, nums: list[int], target: int) -> int:
        nums.sort()
        result = nums[0] + nums[1] + nums[2]

        for i in range(len(nums) - 2):
            left, right = i + 1, len(nums) - 1

            while left < right:
                total = nums[i] + nums[left] + nums[right]

                if abs(target - total) < abs(target - result):
                    result = total

                if total == target:
                    return target
                elif total < target:
                    left += 1
                else:
                    right -= 1

        return result