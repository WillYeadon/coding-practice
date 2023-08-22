class Solution:
    def setZeroes(self, matrix):
        """
        Do not return anything, modify matrix in-place instead.
        """
        eyes = []
        jays = []
        m = len(matrix)
        n = len(matrix[0])

        for i in range(m):
            for j in range(n):
                if matrix[i][j] == 0:
                    eyes.append(i)
                    jays.append(j)

        for k in eyes:
            for j in range(n):
                matrix[k][j] = 0
        for k in jays:
            for i in range(m):
                matrix[i][k] = 0
