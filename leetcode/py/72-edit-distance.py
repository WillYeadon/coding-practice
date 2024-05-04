class Solution:
    def minDistance(self, word1: str, word2: str) -> int:
        m = len(word1) + 1
        n = len(word2) + 1
        matrix = [[0 for _ in range(n)] for _ in range(m)]

        for x in range(m):
            matrix[x][0] = x
        for y in range(n):
            matrix[0][y] = y

        for i in range(1, m):
            for j in range(1, n):
                if word1[i-1] == word2[j-1]:
                    cost = 0
                else:
                    cost = 1
                u = matrix[i][j-1] + 1
                l = matrix[i-1][j] + 1
                d = matrix[i-1][j-1] + cost

                matrix[i][j] = min(u,l,d)

        return matrix[m-1][n-1]