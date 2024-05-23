from typing import Optional
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def rangeSumBST(self, root: Optional[TreeNode], low: int, high: int) -> int:
        ans = []
        def dfs(node):
            if node:
                ans.append(node.val)
                dfs(node.left)
                dfs(node.right)
        dfs(root)
        x = sorted(ans)
        return sum(x[x.index(low):x.index(high) + 1])