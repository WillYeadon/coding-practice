from typing import Optional, List

class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        dp = [0] * (len(cost) + 1)
        for i in range(2, len(dp)):
            dp[i] = min(dp[i-1] + cost[i-1], dp[i-2] + cost[i-2])
        return dp[-1]

x = Solution()
print(x.minCostClimbingStairs([10,15,20]))
print(x.minCostClimbingStairs([1,100,1,1,1,100,1,1,100,1]))