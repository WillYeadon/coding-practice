class Solution:
    def findMin(self, nums):
        l, r = 0, len(nums) - 1
        
        while l <= r:
            if abs(r - l) <= 3:
                return min(nums)
            mid = (l + r) // 2
            # check if mid lower then edges
            if (nums[l] > nums[mid]) and (nums[mid] < nums[r]):
                r = mid
            # check if mid higher then edges
            elif (nums[l] < nums[mid]) and (nums[mid] > nums[r]):
                l = mid
            # else sorted
            else:
                return nums[l]