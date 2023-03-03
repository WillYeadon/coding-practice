from collections import deque
from typing import List

class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        if not grid:
            return 0

        def dfs(i, j):
            # Check you're within bounds
            if i < 0 or i >= len(grid) or j < 0 or j >= len(grid[0])\
                or grid[i][j] != '1':
                # ^ And that you don't have another one e.g. you're
                # at the end 
                return
            # To avoid a separate 'seen' list just modify in place
            # to an 'x' for each value looked at.
            grid[i][j] = 'x'
            # dfs is called when you hit a '1' and then this cascades
            # outwards from that '1' setting all values touched to
            # 'x'
            dfs(i+1, j)
            dfs(i-1, j)
            dfs(i, j+1)
            dfs(i, j-1)

        # Keeps track of the number of islands
        island_count = 0
        # Loop through x and y of the grid
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                # If you have found a 1, recusively flood outwards
                # changing every 1 seen to a 'x'
                if grid[i][j] == '1':
                    dfs(i, j)
                    # Add one for the island you've just flooded
                    island_count += 1

        # return the count
        return island_count


x = Solution()
print(x.numIslands(grid = [
  ["1","1","1","1","0"],
  ["1","1","0","1","0"],
  ["1","1","0","0","0"],
  ["0","0","0","0","0"]
                          ]))
print(x.numIslands(grid = [
  ["0","1","0"],
  ["1","0","1"],
  ["0","1","0"]
                          ]))
print(x.numIslands(grid = [
  ["1","0","1"],
  ["0","1","0"],
  ["1","0","1"]
                          ]))
print(x.numIslands(grid = [
  ["1","0","0"],
  ["0","0","0"],
  ["0","0","0"]
                          ]))
