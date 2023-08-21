class Solution:
    def helper(self, root):
        # Base Case
        if not root:
            return 0, True

        # Recursively find depth and balance for left child
        left_depth, left_balanced = self.helper(root.left)
        
        # Recursively find depth and balance for right child
        right_depth, right_balanced = self.helper(root.right)

        # Check balance condition for current node
        if abs(left_depth - right_depth) > 1:
            return 0, False

        # Return depth and balance status for the tree rooted at the current node
        return 1 + max(left_depth, right_depth), left_balanced and right_balanced

    def isBalanced(self, root):
        _, balanced = self.helper(root)
        return balanced
