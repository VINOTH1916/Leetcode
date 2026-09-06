class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        left = 0

        right = len(matrix[0])*len(matrix) - 1

        n = len(matrix[0])

        while left <= right:
            mid = (left + right) // 2

            row = mid// n
            col = mid % n

            if matrix[row][col] < target:
                left = mid + 1
            elif matrix[row][col] > target:
                right = mid - 1

            else:
                return True

        return False
