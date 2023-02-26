from typing import Optional

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:  
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        def helper(node, lower=float('-inf'), upper=float('inf')):
            # If at end e.g. None then return True as
            # valid BST to have one / no children
            if not node:
                return True
            # Reset val
            val = node.val
            # If it is lower= than lower bound or higher= than
            # upper bound pass up False as not valid BST
            if val <= lower or val >= upper:
                return False
            # These enable the false calls to pass upwards 
            # e.g not False is True so False is returned 
            # upwards and upwards for the right node and left node
            # This can only be triggered if at some point 
            # if val <= lower or val >= upper return False

            # val will become either new lower bound for RHS
            if not helper(node.right, val, upper):
                return False
            # or new upper bound for LHS
            if not helper(node.left, lower, val):
                return False
            # End catch returns True upwards
            return True

        return helper(root)
    
root = TreeNode(4)
root.left = TreeNode(2)
root.right = TreeNode(6)
root.left.left = TreeNode(1)
root.left.right = TreeNode(3)
root.right.left = TreeNode(5)
root.right.right = TreeNode(7)

x = Solution()
print(x.isValidBST(root))