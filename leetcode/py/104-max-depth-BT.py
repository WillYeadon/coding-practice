class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def dfs(self, node):
        if not node:
            return 0
        
        depthLeft = self.dfs(node.left)
        depthRight = self.dfs(node.right)
        
        return max(depthLeft, depthRight) + 1

    def maxDepth(self, root):
        if not root:
            return 0
        return self.dfs(root)
