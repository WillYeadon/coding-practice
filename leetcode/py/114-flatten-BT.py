class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def dfs_preorder(self, root):
        if not root:
            return []
        result = []
        result.append(root)
        result.extend(self.dfs_preorder(root.left))
        result.extend(self.dfs_preorder(root.right))
        return result

    def flatten(self, root):
        """
        Do not return anything, modify root in-place instead.
        """
        if not root: return 
        order = self.dfs_preorder(root)
        root = order.pop(0)
        for i in order:
            root.right = i
            root.left = None
            root = root.right
        return 
