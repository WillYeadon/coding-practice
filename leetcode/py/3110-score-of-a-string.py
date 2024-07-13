class Solution:
    def scoreOfString(self, s: str) -> int:
        nums = []
        for c in s:
            nums.append(ord(c))
        ans = 0
        for i in range(len(nums) - 1):
            ans += abs(nums[i] - nums[i + 1])
        return ans