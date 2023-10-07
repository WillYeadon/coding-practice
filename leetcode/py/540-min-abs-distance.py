from typing import Optional
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def __init__(self):
        self.prev_node = None
        self.min_diff = float('inf')
        
    def helper(self, root):
        if root is None:
            return
        self.helper(root.left)
        if self.prev_node is not None:
            self.min_diff = min(self.min_diff, root.val - self.prev_node.val)
        self.prev_node = root
        self.helper(root.right)
        
    def getMinimumDifference(self, root: Optional[TreeNode]) -> int:
        self.helper(root)
        return self.min_diff