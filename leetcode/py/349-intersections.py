from typing import List
class Solution:
    def intersection(self, nums1: List[int], nums2: List[int]) -> List[int]:
        return set(nums1) & set(nums2)

        s, l = nums1, nums2
        if len(nums1) >= len(nums2):
            s, l = nums2, nums1
        ans = []
        for i in s:
            if i in l and i not in ans:
                ans.append(i)
        return ans