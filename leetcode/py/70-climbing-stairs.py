class Solution:
    def climbStairs(self, n: int) -> int:
        memo = {}
        
        def helper(n):
            if n < 1:
                return 0
            elif n == 1:
                return 1
            elif n == 2:
                return 2
            elif n in memo:
                return memo[n]
            else:
                memo[n] = helper(n - 1) + helper(n - 2)
                return memo[n]
        
        return helper(n)

x = Solution()
print(x.climbStairs(10))
print(x.climbStairs(15))
print(x.climbStairs(40))