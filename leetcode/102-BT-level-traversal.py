from typing import List, Optional
from collections import deque

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if root is None:
            return []

        queue = deque([(root, 0)])
        result = []

        while queue:
            node, level = queue.popleft()

            if level == len(result):
                result.append([])

            result[level].append(node.val)

            if node.left:
                queue.append((node.left, level + 1))
            if node.right:
                queue.append((node.right, level + 1))

        return result

x = Solution()
root = TreeNode(1, left=TreeNode(2), 
                right=TreeNode(3, left=TreeNode(4), right=TreeNode(5))) 
print(x.levelOrder(root))