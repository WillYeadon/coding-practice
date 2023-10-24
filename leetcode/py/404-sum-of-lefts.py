# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def sumOfLeftLeaves(self, root) -> int:
        if not root:
            return

        lefts = []
        if root.left:
            if not root.left.left and not root.left.right:
                lefts.append(root.left.val)
            else:
                lefts.append(self.sumOfLeftLeaves(root.left))
    
        if root.right:
            lefts.append(self.sumOfLeftLeaves(root.right))

        return sum(lefts)