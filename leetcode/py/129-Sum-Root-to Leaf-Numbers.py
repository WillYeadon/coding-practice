# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    overall = 0

    def preorder(self, root, vals):
        if root:
            vals.append(root.val)
            if not root.left and not root.right:
                s = ''
                for i in vals:
                    s += str(i)
                self.overall += int(s)
                #print(int(s), self.overall)
                vals.pop()
            else:
                self.preorder(root.left, vals)
                self.preorder(root.right, vals)
                vals.pop()
        
    def sumNumbers(self, root):
        self.preorder(root, [])
        return self.overall