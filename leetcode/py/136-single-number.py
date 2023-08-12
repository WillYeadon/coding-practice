class Solution:
    def singleNumber(self, nums):
        vals = {}
        for i in nums:
            if i not in vals:
                vals[i] = 1
            else:
                vals[i] += 1
        for j in vals.keys():
            if vals[j] == 1:
                return j
        return -1