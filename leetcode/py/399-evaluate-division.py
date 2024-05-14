from collections import defaultdict
from typing import List

class Solution:
    def calcEquation(self, equations: List[List[str]], values: List[float], queries: List[List[str]]) -> List[float]:       
        def dfs(graph, start, end, visited, value):
            if start not in graph or end not in graph:
                return -1.0
            if start == end:
                return value
            visited.add(start)
            for neighbor, val in graph[start].items():
                if neighbor not in visited:
                    result = dfs(graph, neighbor, end, visited, value * val)
                    if result != -1.0:
                        return result
            visited.remove(start)
            return -1.0

        graph = defaultdict(dict)
        for (num, den), value in zip(equations, values):
            graph[num][den] = value
            graph[den][num] = 1 / value
        
        results = []
        for num, den in queries:
            if num in graph and den in graph:
                results.append(dfs(graph, num, den, set(), 1.0))
            else:
                results.append(-1.0)
        
        return results