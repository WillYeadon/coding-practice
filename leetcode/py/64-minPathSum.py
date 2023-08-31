class Solution:
    def minPathSum(self, grid):
        rows = len(grid)
        cols = len(grid[0])

        for i in range(rows):
            for j in range(cols):
                up = 201
                left = 201                
                if j > 0:
                    left = grid[i][j - 1]
                if i > 0:
                    up = grid[i - 1][j]
                if i > 0 or j > 0:
                    grid[i][j] += min(left, up)


        return grid[-1][-1]