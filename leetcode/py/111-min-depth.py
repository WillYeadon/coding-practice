# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def helper(self, root, level):
        if not root:
            return float('inf')  # Return infinity if node is None, not level

        if not root.left and not root.right:  # If it's a leaf node
            return level + 1

        leftDepth = self.helper(root.left, level + 1)
        rightDepth = self.helper(root.right, level + 1)

        return min(leftDepth, rightDepth)  # No need to add 1 here

    def minDepth(self, root):
        if not root:  # Edge case where the tree is empty
            return 0
        return self.helper(root, 0)

