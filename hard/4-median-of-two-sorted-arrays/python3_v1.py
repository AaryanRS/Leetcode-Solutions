# Pushed: 2026-09-08 04:29:10 UTC
# Difficulty: Hard
# Runtime: 0 ms
# Memory: 19.5 MB

class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        nums1.extend(nums2)
        nums1.sort()
        n = len(nums1)

        if n % 2 == 1:
            return float(nums1[n // 2])
        else:
            return (nums1[n // 2 - 1] + nums1[n // 2]) / 2.0
