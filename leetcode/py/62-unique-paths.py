class SolutionA:
    def uniquePaths(self, m: int, n: int) -> int:
        def helper(m, n, x=0, y=0):
            if x == m-1 and y == n-1:
                return 1
            if x >= m or y >= n:
                return 0
            return helper(m, n, x+1, y) + helper(m, n, x, y+1)

        return helper(m, n)

class SolutionB:
    def uniquePaths(self, m: int, n: int) -> int:
        # Initialize the memoization table with 0
        memo = [[0] * n for _ in range(m)]
        
        # Define the helper function with memoization
        def helper(x, y):
            # If the current cell is outside the grid, return 0
            if x >= m or y >= n:
                return 0
            
            # If we've already computed the result for this cell, return it
            if memo[x][y] != 0:
                return memo[x][y]
            
            # Base case: if we've reached the bottom-right corner of the grid, return 1
            if x == m-1 and y == n-1:
                memo[x][y] = 1
            else:
                # Otherwise, compute the result recursively and store it in the memoization table
                memo[x][y] = helper(x+1, y) + helper(x, y+1)
                
            return memo[x][y]
        
        # Call the helper function with the starting coordinates (0,0)
        return helper(0, 0)


    
x = SolutionA()
print(x.uniquePaths(3, 7))
print(x.uniquePaths(3, 2))

y = SolutionB()
print(y.uniquePaths(3, 7))
print(y.uniquePaths(3, 2))
