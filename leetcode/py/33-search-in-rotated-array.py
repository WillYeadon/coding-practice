class Solution:
    def search(self, nums, target):
        l, r = 0, len(nums) - 1
        while l <= r:
            mid = (l + r) // 2
            if nums[mid] == target:
                return mid
            if nums[l] <= nums[mid]:   ## LHS must be sorted in this case
                if nums[l] <= target < nums[mid]: # target in this sorted part?
                    r = mid - 1
                else: # target not in sorted mark hence l to the right
                    l = mid + 1 # of that middle bit
            else:  ## RHS must be sorted
                if nums[mid] < target <= nums[r]: # target in this sorted part?
                    l = mid + 1
                else:
                    r = mid - 1
        return -1