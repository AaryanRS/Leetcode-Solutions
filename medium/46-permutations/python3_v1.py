# Pushed: 2026-09-30 09:37:44 UTC
# Difficulty: Medium
# Runtime: 0 ms
# Memory: 19.6 MB

class Solution:
    def permute(self, nums: list[int]) -> list[list[int]]:
        res = []
        start = 0
        def permutation(index, temp):
            if index >= len(nums):
                res.append(temp.copy())
                return 
            for i in range(index, len(nums)):
                nums[index], nums[i] = nums[i], nums[index]
                temp.append(nums[index])
                permutation(index + 1, temp)
                temp.pop()
                nums[index], nums[i] = nums[i], nums[index]

        permutation(0, [])
        return res
