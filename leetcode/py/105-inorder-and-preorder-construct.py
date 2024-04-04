# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def buildTree(self, preorder, inorder):
        if not preorder or not inorder:
            return None
        
        # The first element in preorder is always the root.
        root = TreeNode(preorder[0])
        # Find the index of the root in inorder list.
        mid = inorder.index(preorder[0])
        
        # Recursively construct the left and right subtree.
        # Exclude the root element from the inorder list for the right subtree by starting from mid + 1
        root.left = self.buildTree(preorder[1:mid+1], inorder[:mid])
        root.right = self.buildTree(preorder[mid+1:], inorder[mid+1:])
        
        return root
