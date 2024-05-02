class Solution:
    def singleNumber(self, nums):
        count = {}
        for n in nums:
            if n not in count:
                count[n] = 1
            else:
                count[n] += 1
        for k in count.keys():
            if count[k] == 1:
                return k