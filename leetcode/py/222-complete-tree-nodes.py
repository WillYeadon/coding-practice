from collections import deque
from typing import Optional

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def countNodes(self, root: Optional[TreeNode]) -> int:
        vals = []
        que = deque([root])
        
        while que:
            node = que.popleft()
            if node:
                vals.append(node.val)
                if node.left:
                    que.append(node.left)
                if node.right:
                    que.append(node.right)

        return len(vals)