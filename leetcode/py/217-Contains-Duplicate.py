class Solution:
    def containsDuplicate(self, nums):
        x = {}
        for i in nums:
            if i not in x:
                x[i] = 1
            else:
                return True
        return False