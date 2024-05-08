class Solution:
    def searchRange(self, nums, target):        
        l, r = 0, len(nums) - 1
        if r == -1:
            return [-1, -1]
        if r == 0:
            return [0, 0] if nums[0] == target else [-1, -1]
        start = -1
        while l <= r:
            mid = (l + r) // 2
            if nums[mid] == target:
                start = mid
                break
            elif nums[mid] > target:
                r = mid - 1
            else:
                l = mid + 1

        if start == -1:
            return [-1, -1]
        else:
            left, right = start, start
            while left > 0 and nums[left - 1] == target:
                left -= 1
            while right < len(nums) - 1 and nums[right + 1] == target:
                right += 1
            return [left, right]