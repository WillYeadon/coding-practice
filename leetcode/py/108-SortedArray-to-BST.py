from typing import List

class TreeNode:
     def __init__(self, val=0, left=None, right=None):
         self.val = val
         self.left = left
         self.right = right
class Solution:
    def sortedArrayToBST(self, nums: List[int]):
        length = len(nums)
        if length == 0:
            return
        elif length < 2:
            return TreeNode(nums[0])
        mid = length // 2
        head = TreeNode(nums[mid])
        left = nums[:mid]
        right = nums[mid + 1:]

        head.left = self.sortedArrayToBST(left)
        head.right = self.sortedArrayToBST(right)

        return head
