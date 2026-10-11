# Pushed: 2026-10-11 06:08:49 UTC
# Difficulty: Medium
# Runtime: 3 ms
# Memory: 20.7 MB

class Solution(object):
    def setZeroes(self, matrix):
        zeroinFirstCol = False
        for row in range(len(matrix)):
            if matrix[row][0] == 0:
                zeroinFirstCol = True
            for col in range(1, len(matrix[0])):
                if matrix[row][col] == 0:
                    matrix[row][0] = 0
                    matrix[0][col] = 0

        for row in range(len(matrix) - 1, -1, -1):
            for col in range(len(matrix[0]) - 1, 0, -1):
                if matrix[row][0] == 0 or matrix[0][col] == 0:
                    matrix[row][col] = 0
            if zeroinFirstCol:
                matrix[row][0] = 0