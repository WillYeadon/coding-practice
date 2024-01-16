from typing import List
class Solution:
    def kidsWithCandies(self, candies: List[int], extraCandies: int) -> List[bool]:
        added = [x + extraCandies for x in candies]
        ans = [False] * len(added)
        maxC = max(candies)
        for i, v in enumerate(added):
            if v >= maxC:
                ans[i] = True
        return ans