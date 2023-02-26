from typing import List

class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children

class Solution:
    def preorder(self, root: 'Node') -> List[int]:
        if not root:
            return
        
        pot = [root.val]

        if root.children:
            for child in root.children:
                 pot += self.preorder(child)

        return pot
    
x = Solution()
root = Node(1, [Node(2), Node(3, [Node(4), Node(5)]), Node(6)])
print(x.preorder(root))