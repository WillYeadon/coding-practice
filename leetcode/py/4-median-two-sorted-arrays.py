class Solution:
    def findMedianSortedArrays(self, nums1, nums2):
        x = sorted(nums1 + nums2)
        y = len(x)
        if y == 1:
            return x[0]
        elif y % 2 == 0:
            return 0.5 * (x[(y // 2) - 1] + x[(y // 2)])
        else:
            return x[y // 2]