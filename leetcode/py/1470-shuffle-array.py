class Solution:
    def shuffle(self, nums, n):
        l = len(nums) // 2
        a = nums[0:l]
        b = nums[l:]
        ans = []
        for i,j in zip(a,b):
            ans.append(i)
            ans.append(j)
        return ans