from typing import List
class Solution:
    def summaryRanges(self, nums: List[int]) -> List[str]:
        ans = []
        nums.append(-1000)
        index = 0
        while index < len(nums[:-1]):
            start = index
            end = index + 1
            if (nums[end] - nums[start]) == 1:
                firstStart = start
                while (nums[end] - nums[start]) == 1:
                    start += 1
                    end += 1
                string = str(nums[firstStart]) + '->' + str(nums[end-1])
                ans.append(string)
            else:
                ans.append(str(nums[start]))
            index = end
        return ans
        