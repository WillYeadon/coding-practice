from collections import deque

class Node:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None

def dfs(root, visited=[]):
    if root:
        dfs(root.left, visited)
        visited.append(root)
        dfs(root.right, visited)
    
    return visited

def bfs(root):
    visited = []
    queue = deque([root])

    while queue:
        node = queue.popleft()
        visited.append(node)

        if node.left:
            queue.append(node.left)
        if node.right:
            queue.append(node.right)

    return visited

root = Node(4)
root.left = Node(2)
root.right = Node(6)
root.left.left = Node(1)
root.left.right = Node(3)
root.right.left = Node(5)
root.right.right = Node(7)

visited_nodes = dfs(root)
print([node.val for node in visited_nodes])
visited_nodes = bfs(root)
print([node.val for node in visited_nodes])

y = [1,2,3,4]
z = [3,4,5,6]
both = [x for x in y if x in z]
print(both)