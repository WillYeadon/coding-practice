from collections import deque

class Node:
    def __init__(self, val: int = 0, left: 'Node' = None, right: 'Node' = None, next: 'Node' = None):
        self.val = val
        self.left = left
        self.right = right
        self.next = next

class Solution:
    def bfs(self, root):
        if not root:
            return []
        
        queue = deque([root])
        result = []

        while queue:
            level_size = len(queue)
            current_level = []

            for _ in range(level_size):
                node = queue.popleft()
                current_level.append(node)

                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)
            result.append(current_level)

        return result

    def connect(self, root: 'Node') -> 'Node':
        if not root: return root
        bfs = self.bfs(root)
        
        while len(bfs) > 0:
            level = bfs.pop(0)
            for i in range(len(level) - 1):
                level[i].next = level[i + 1]

        return root