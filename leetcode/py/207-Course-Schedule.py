from typing import List
class Solution:
    def has_cycle(self, graph):
        recursion_stack = set()
        visited = set()

        def dfs(node):
            if node in recursion_stack:
                return True
            if node in visited:
                return False

            visited.add(node)
            recursion_stack.add(node)

            for neighbor in graph.get(node, []):
                if dfs(neighbor):
                    return True
            recursion_stack.remove(node)
            return False

        for node in graph:
            if not node in visited:
                if dfs(node):
                    return True
        return False

    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        reqs = {}
        for req in prerequisites:
            if req[0] not in reqs:
                reqs[req[0]] = [req[1]]
            else:
                reqs[req[0]].append(req[1])
        # want to check that athere is no tortology
        #print(reqs)
        if self.has_cycle(reqs):
            return False

        return True