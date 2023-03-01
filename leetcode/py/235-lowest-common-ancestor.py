class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

# Create the root node
root = TreeNode(1)

# Create the second layer nodes
node2 = TreeNode(2)
node3 = TreeNode(3)

# Create the third layer nodes
node4 = TreeNode(4)
node5 = TreeNode(5)
node6 = TreeNode(6)
node7 = TreeNode(7)

# Create the fourth layer nodes
node8 = TreeNode(8)
node9 = TreeNode(9)
node10 = TreeNode(10)
node11 = TreeNode(11)
node12 = TreeNode(12)
node13 = TreeNode(13)
node14 = TreeNode(14)
node15 = TreeNode(15)

# Connect the nodes to form the tree
root.left = node2
root.right = node3

node2.left = node4
node2.right = node5

node3.left = node6
node3.right = node7

node4.left = node8
node4.right = node9

node5.left = node10
node5.right = node11

node6.left = node12
node6.right = node13

node7.left = node14
node7.right = node15

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        rv = root.val
        pv = p.val
        qv = q.val

        if (pv < rv) and (qv < rv):
            while (root.left and pv < root.left.val and qv < root.left.val):
                root = root.left
            return self.lowestCommonAncestor(root.left, p, q)

        elif (pv > rv) and (qv > rv):
            while (root.right and pv > root.right.val and qv > root.right.val):
                root = root.right
            return self.lowestCommonAncestor(root.right, p, q)

        else:
            return root
        
solution = Solution()
lca = solution.lowestCommonAncestor(root, node3, node10)
print(lca.val)  