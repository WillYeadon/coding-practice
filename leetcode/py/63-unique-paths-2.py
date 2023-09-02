class Solution:
    def uniquePathsWithObstacles(self, obstacleGrid):
        m = len(obstacleGrid)
        n = len(obstacleGrid[0])
        memo = [[0] * n for _ in range(m)]

        def helper(x, y):
            # out of bounds
            if (x >= m or y >= n or obstacleGrid[x][y] == 1):
                return 0
            # check memod
            if memo[x][y] != 0:
                return memo[x][y]
            # base
            if x == m - 1 and y == n -1:
                return 1
            else:
                memo[x][y] = helper(x + 1, y) + helper(x, y + 1)
            
            return memo[x][y]

        return helper(0,0)