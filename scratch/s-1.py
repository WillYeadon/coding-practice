class Node:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None

def traverse(root, func):
    if root:
        traverse(root.left, func)
        func(root)
        traverse(root.right, func)

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
