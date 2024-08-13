class Solution:
    def dfs(self, node, target, visited=None, visited_values=None):
        if visited is None:
            visited = []
        if visited_values is None:
            visited_values = []
            
        visited.append(node)
        visited_values.append(node.val)
        
        if node.val == target:
            return visited, visited_values
        
        if node.left is not None:
            left_visited, left_visited_values = self.dfs(node.left, target, visited, visited_values)
            if left_visited:
                return left_visited, left_visited_values
        
        if node.right is not None:
            right_visited, right_visited_values = self.dfs(node.right, target, visited, visited_values)
            if right_visited:
                return right_visited, right_visited_values
            
        return None, None

    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        if (not root) or (not p) or (not q):
            return None

        visitedP, visitedPL = self.dfs(root, p.val)
        visitedQ, visitedQL = self.dfs(root, q.val)

        if visitedP and visitedQ:
            for node in reversed(visitedP):
                if node in visitedQ:
                    return node
        
        return None

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

solution = Solution()
p = TreeNode(8)
q = TreeNode(10)
lca = solution.lowestCommonAncestor(root, p, q)
print(lca.val)  # Output: 2
