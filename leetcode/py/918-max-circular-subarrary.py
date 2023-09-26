from typing import List

class Solution:
    def maxSubarraySumCircular(self, nums: List[int]) -> int:
        max_kadane = max_current = nums[0]
        min_kadane = min_current = nums[0]
        total_sum = nums[0]

        for num in nums[1:]:
            max_current = max(num, max_current + num)
            max_kadane = max(max_kadane, max_current)
            
            min_current = min(num, min_current + num)
            min_kadane = min(min_kadane, min_current)

            total_sum += num

        if max_kadane < 0:
            return max_kadane
        return max(max_kadane, total_sum - min_kadane)
