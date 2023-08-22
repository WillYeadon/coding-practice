# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def postorderTraversal(self, root):
        if not root:
            return []
        
        one = [root]
        two = []
        vals = []

        while one:
            node = one.pop()
            two.append(node)

            if node.left:
                one.append(node.left)
            if node.right:
                one.append(node.right)

        while two:
            vals.append(two.pop().val)

        return vals