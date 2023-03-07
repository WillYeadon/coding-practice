from math import factorial

class SolutionA:
    def uniquePaths(self, m: int, n: int) -> int:
        def helper(m, n, x=0, y=0):
            # It is only a path if you have reached x = m-1 and
            # y = n-1 at the end of the recursion stack
            if x == m-1 and y == n-1:
                return 1
            # Out of bounds so noth a path
            if x >= m or y >= n:
                return 0
            # Return the total of going right (x+1) and down (y+1)
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

class SolutionC:
    # There is a third combinatorics method. Although this
    # is very difficult to work out without knowing it in advance
    def uniquePaths(self, m: int, n: int) -> int:      
        return factorial((m-1) + (n-1)) // (factorial(m-1)* factorial(n-1))

    
x = SolutionA()
print(x.uniquePaths(3, 7), x.uniquePaths(3, 2))

y = SolutionB()
print(y.uniquePaths(3, 7), y.uniquePaths(3, 2))

z = SolutionC()
print(z.uniquePaths(3, 7), z.uniquePaths(3, 2))

