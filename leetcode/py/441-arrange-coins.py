class Solution:
    def arrangeCoins(self, n: int) -> int:
        stairs = 0
        level = 1
        while n >= level:
            n -= level
            level += 1
            stairs += 1
        return stairs