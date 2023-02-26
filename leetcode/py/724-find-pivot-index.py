from typing import List

class Solution:
    def pivotIndex(self, nums: List[int]) -> int:
        # Only sum all once
        sumAll = sum(nums)
        sumLeft = 0
        
        for i, num in enumerate(nums):
            # sumRight is the sum of all the numbers minus
            # the sum of all numbers left of the pivot
            # minus the num at the pivot point
            sumRight = sumAll - sumLeft - num
            # If sumLeft == sumRight you're at the pivot
            if sumLeft == sumRight:
                return i
            # Else increase sumLeft by num
            sumLeft += num
        
        return -1
        
x = Solution()

# Expect 3
print(x.pivotIndex([1,7,3,6,5,6]))

# Expect 3
print(x.pivotIndex([-1,-1,0,-1,-1,-1]))

# Expect 0
print(x.pivotIndex([-1,-1,-1,0,1,1]))

# Expect 2
print(x.pivotIndex([-1,-1,0,-1,-1,0]))

# Expect 4
print(x.pivotIndex([-1,-1,0,1,0,-1]))