from typing import List
class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        end = -1
        noChange = True
        while noChange:
            noChange = False
            for i in range(len(nums[:end])):
                if nums[i] == 0 and nums[i + 1] != 0:
                    nums[i] = nums[i + 1]
                    nums[i + 1] = 0
                    noChange = True   
            if nums[end] == 0:
                end -= 1 

class SolutionFast:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        l = 0 # left pointer at beginning
        for r in range(len(nums)): # right pointer iterate through whole list
            if nums[r]: # not 0
                nums[l], nums[r] = nums[r], nums[l] # swap left with right, right with left
                l += 1 # increment left index
        return nums # return updated list
            