# The key element here is that the local diameter is the diameter
# from the left and right nodes from any root

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def __init__(self):
        self.max_diameter = 0  

    def depth(self, node):
        # Null contributes zero to depth
        if not node:
            return -1     
        # left & right depth
        left_height = self.depth(node.left)  
        right_height = self.depth(node.right)
        # Total diameter will be the left & right heights plus the 
        # edges connecting them e.g.
        #   b 
        #  / \
        # a   c
        current_diameter = left_height + right_height + 2
        # Update the current max diameter, if at all
        self.max_diameter = max(self.max_diameter, current_diameter)     
        # Return the height of this node e.g. the max of left & right
        # plus 1 for this current node
        return max(left_height, right_height) + 1

    def diameterOfBinaryTree(self, root):
        self.depth(root)
        return self.max_diameter