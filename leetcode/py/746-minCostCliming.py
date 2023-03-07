from typing import Optional, List

class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        # Create a dp array to store the minimum cost of 
        # climbing to each step
        dp = [0] * (len(cost) + 1)
        
        # Iterate through the steps starting at the third step (index 2)
        for i in range(2, len(dp)):
            # Calculate the minimum cost of reaching the i-th step
            # by either coming from the previous step (i-1)
            # or the step before that (i-2),
            # and adding the cost of the current step (i-1 or i-2)
            dp[i] = min(dp[i-1] + cost[i-1], dp[i-2] + cost[i-2])
        
        # Return the last element of the dp array, which represents 
        # the minimum cost of reaching the top of the staircase 
        # (either the last step or the step before it)
        return dp[-1]

x = Solution()
print(x.minCostClimbingStairs([10,15,20]))
print(x.minCostClimbingStairs([1,100,1,1,1,100,1,1,100,1]))