# Pushed: 2026-09-27 05:06:49 UTC
# Difficulty: Medium
# Runtime: 3145 ms
# Memory: 22.6 MB

class Solution:
    def threeSum(self, nums: list[int]) -> list[list[int]]:
        result = set()

        for i in range(len(nums)):
            my_set = set()
            for j in range(i+1,len(nums)):
                third = -(nums[i]+nums[j])
                if third in my_set:                     # TC = O(N^2), SC = O(N) + O(no. of triplets)
                    temp = [nums[i],nums[j],third]
                    temp.sort()
                    result.add(tuple(temp))
                my_set.add(nums[j])

        return list(result)