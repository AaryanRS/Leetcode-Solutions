# Pushed: 2026-09-27 05:56:56 UTC
# Difficulty: Medium
# Runtime: 992 ms
# Memory: 19.2 MB

class Solution:
    def fourSum(self, nums: list[int], target: int) -> list[list[int]]:
        result = set()

        for i in range(len(nums)):
            for j in range(i+1,len(nums)):
                my_set = set()
                for k in range(j+1,len(nums)):
                    fouth = target-(nums[i]+nums[j]+nums[k])
                    if fouth in my_set:
                        temp = [nums[i],nums[j],nums[k],fouth]
                        temp.sort()
                        result.add(tuple(temp))
                    my_set.add(nums[k])

        return list(result)