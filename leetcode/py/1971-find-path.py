from collections import defaultdict
from typing import List

class Solution:
    def validPath(self, n: int, edges: List[List[int]], source: int, destination: int) -> bool:
        if source == destination:
            return True
        graph = defaultdict(list)
        for x,y in edges:
            graph[x].append(y)
            graph[y].append(x)
        seen = set()
        stack = []
        seen.add(source)
        stack.append(source)
        while stack:
            node = stack.pop()
            for x in graph[node]:
                if x == destination:
                    return True
                if x not in seen:
                    seen.add(x)
                    stack.append(x)
        return False