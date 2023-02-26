from collections import deque

class Node:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None

def traverse(root, func):
    # If not at end
    if root:
        # Call left repeatedly until at end
        traverse(root.left, func)
        # Apply func
        func(root)
        # Call right
        traverse(root.right, func)

def traverseBFS(root, func):
    if not root:
        return
    queue = deque([root])
    while queue:
        node = queue.popleft()
        func(node)
        if node.left:
            queue.append(node.left)
        if node.right:
            queue.append(node.right)

def check_gt_5(node):
    if node.val > 5:
        print(f'{node.val} is greater than 5')

root = Node(4)
root.left = Node(2)
root.right = Node(6)
root.left.left = Node(1)
root.left.right = Node(3)
root.right.left = Node(5)
root.right.right = Node(7)

traverse(root, check_gt_5)
traverseBFS(root, check_gt_5)