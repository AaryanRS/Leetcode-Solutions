# Pushed: 2026-09-17 16:26:00 UTC
# Difficulty: Medium
# Runtime: 0 ms
# Memory: 19.6 MB

class Solution:
    def searchMatrix(self, matrix: list[list[int]], target: int) -> bool:
        
        m = len(matrix)
        n = len(matrix[0])

        low = 0
        high = (m*n)-1      # I converted this to 1-D Matrix

        while low <= high:
            mid = (low+high)//2

            # Now i will convert 1-D to 2-D

            row = mid//n
            col = mid%n

            mid_element = matrix[row][col]

            if mid_element == target:
                return True
            elif mid_element < target:
                low = mid+1
            else:
                high = mid-1
        return False