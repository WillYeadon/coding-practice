from typing import List

class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        # Leave early if invalid
        if (len(prices) == 0) or (len(prices) == 1):
            return 0

        # Take first value as min
        min_price = prices[0]
        # Start at zero
        max_profit = 0
    
        # Out of the remaining prices
        for price in prices[1:]:
            # Profit is difference between price and min
            profit = price - min_price
            
            # If new profit bigger than old, update
            if profit > max_profit:
                max_profit = profit

            # If you are at a point in the array where there is a lower number
            # any subsequent higher number would represent a profit. So for
            # [2,3,4,1,5] initially 2 is chosen and is lower than 3 or 4 and
            # the max seen profit is 2 (4 - 2 = 2). When 1 is seen it is less
            # than two so is the new lowest price. Any subsequent profit 
            # derived from X - 1 will be thus larger than X - 2. Remember this
            # is profit so there may not be a more profitable trade available
            # however, if there is X - 1 > X - 2.
            if price < min_price:
                min_price = price
    
        return max_profit
            
x = Solution()
print(x.maxProfit([2,4,1]))
print(x.maxProfit([7,6,4,3,1]))