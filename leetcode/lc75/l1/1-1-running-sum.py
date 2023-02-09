from typing import List

class Solution:
    def runningSum(self, nums: List[int]) -> List[int]:
        ans = []
        running_sum = 0
        for num in nums:
            running_sum += num
            ans.append(running_sum)

        return ans
    
x = Solution()

# Expect [1,3,6,10]
print(x.runningSum([1,2,3,4]))

# Expect [2,6,12,20]
print(x.runningSum([2,4,6,8]))