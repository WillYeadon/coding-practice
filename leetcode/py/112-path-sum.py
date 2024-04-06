class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def hasPathSum(self, root, targetSum):
        if not root: return False
        t = targetSum - root.val
        
        if t == 0 and root.left == None and root.right == None:
            return True
        else:
            return self.hasPathSum(root.left, t) or self.hasPathSum(root.right, t)