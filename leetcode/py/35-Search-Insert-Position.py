class Solution:
    def searchInsert(self, nums, target):
        left = 0
        right = len(nums)

        if nums[left] >= target:
            return 0
        if nums[right - 1] < target:
            return right

        pivot = (left + right) // 2

        while (right - left) > 1:
            pivot = (left + right) // 2
            can = nums[pivot]

            if can == target:
                return pivot
            elif can > target:
                right = pivot
            else:
                left = pivot

        return pivot if nums[pivot] >= target else pivot + 1

        


