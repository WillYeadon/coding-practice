class Solution:
    def coinChange(self, coins, amount) -> int:
        # Create a dp list with size amount + 1 and initialize with a large value
        # (float('inf') denotes infinity in Python)
        dp = [float('inf')] * (amount + 1)
        
        # Base case: 0 coins are needed to make up the amount 0
        dp[0] = 0
        
        # Loop through all amounts up to the given amount
        for i in range(1, amount + 1):
            # For each coin denomination in coins
            for coin in coins:
                # Check if the current coin can be used (i.e., it's not larger than the current amount)
                if i - coin >= 0:
                    # If it can be used, update dp[i] with the minimum value between the current dp[i]
                    # and dp[i - coin] + 1. dp[i - coin] + 1 represents using the current coin and
                    # then adding the minimum coins needed for the remaining amount (i - coin).
                    dp[i] = min(dp[i], dp[i - coin] + 1)

        # If the final value is infinity, there's no solution. Otherwise, return the final value.
        return dp[amount] if dp[amount] != float('inf') else -1
