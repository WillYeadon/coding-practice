from typing import List

class SolutionA:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        length = len(nums)
        if length == 2:
            return [0,1]
        
        for i in range(length):
            for j in range(i, length):
                if i != j:
                    if (nums[i] + nums[j] == target):
                        return [i, j]

        return [0,1]

class SolutionB:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        hashed = {}
        i = 0

        while target - nums[i] not in hashed:
            hashed[nums[i]] = i
            i += 1

        return [hashed[target - nums[i]], i]
    
x = SolutionA()
print(x.twoSum([3,2,3], 6))
y = SolutionB()
print(y.twoSum([3,2,3], 6))