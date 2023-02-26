from typing import List

class Solution:
    def search(self, nums: List[int], target: int) -> int:
        left, right = 0, len(nums) - 1
        while left <= right:
            mid = (left + right) // 2
            if nums[mid] == target:
                return mid
            elif nums[mid] < target:
                left = mid + 1
            else:
                right = mid - 1
        return -1
    
x = Solution()
print(x.search([-1,0,3,5,8,12], 5))
print(x.search([2,3,4,7,9,15], 9))
print(x.search([1], 1))
print(x.search([], 1))