from typing import List

class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        stones.sort()

        while len(stones) > 1:
            a = stones.pop()
            b = stones.pop()

            if a <= b:
                x = a
                y = b
            else:
                x = b
                y = a

            if x != y:                
                stones.append(y - x)
            stones.sort()

        if len(stones) == 1:
            return stones[0]
        else:
            return 0
        
x = Solution()
print(x.lastStoneWeight([2,7,4,1,8,1]))
print(x.lastStoneWeight([1]))
print(x.lastStoneWeight([]))