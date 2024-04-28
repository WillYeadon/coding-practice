# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    nodes = []
    def inorder_traversal(self, root):
        if root:
            self.inorder_traversal(root.left)
            self.nodes.append(root.val)
            self.inorder_traversal(root.right)

    def kthSmallest(self, root, k):
        self.nodes = []
        self.inorder_traversal(root)
        return self.nodes[k-1]