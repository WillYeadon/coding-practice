from collections import deque
from typing import Optional
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        o = deque([p])
        t = deque([q])

        while len(o) > 0 and len(t) > 0:
            one = o.popleft()
            two = t.popleft()

            if one:
                o.append(one.left)
                o.append(one.right)
            if two:
                t.append(two.left)
                t.append(two.right)

            if type(one) != type(two):
                return False
            if one and two:
                if not (one.val == two.val):
                    return False 

        return True    