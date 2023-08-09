class Solution:
    def findPeakElementInBuilt(self, nums):
        if len(nums) == 1:
            return 0
        return nums.index(max(nums))
    
    def findPeakElement(self, nums): 
        if len(nums) == 1:
            return 0
        
        left = 0
        right = len(nums) - 1
        mid = (left + right) // 2

        while left < right:
            if nums[mid] > nums[mid + 1]:
                right = mid
            else:
                left = mid + 1
            mid = (left + right) // 2

        return left if nums[left] > nums[right] else right