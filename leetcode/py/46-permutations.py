from typing import List
class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        ans = []
        def backtrack(current, remain):
            if len(current) == len(nums):
                ans.append(current[:])
                return
            for i in range(len(remain)):
                current.append(remain[i])
                backtrack(current, remain[:i] + remain[i+1:])
                # don't forget to pop
                current.pop()

        backtrack([], nums)
        return ans
