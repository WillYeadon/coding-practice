class Solution:
    def searchMatrix(self, matrix, target):
        if not matrix or not matrix[0]: return False # Check for empty rows or columns

        rows, cols = len(matrix), len(matrix[0])
        length = rows * cols
        left, right = 0, length - 1

        while left <= right:
            cur = (left + right) // 2
            row = cur // cols
            col = cur % cols
            can = matrix[row][col]

            if can == target:
                return True
            elif can < target:
                left = cur + 1
            else:
                right = cur - 1
                
        return False



