from typing import List

class Solution:
    def thirdMax(self, nums: List[int]) -> int:
        if len(nums) < 3: return max(nums)
        nums.sort(reverse=True)
        seen = {}
        for i in nums:
            if i not in seen:
                seen[i] = 1
            else:
                seen[i] += 1
        keys = list(seen.keys())
        if len(keys) < 3: return max(nums)
        return keys[2]