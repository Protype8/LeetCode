class Solution:
    def minReorder(self, n: int, connections: List[List[int]]) -> int:
        edges = set()
        neighbors = {city:[] for city in range(n)}
        visited = set()
        changes = 0
        for a,b in connections:
            neighbors[a].append(b)
            neighbors[b].append(a)
            edges.add((a,b))
        def dfs(city):
            nonlocal edges,neighbors,visited,changes
            for neighbor in neighbors[city]:
                if(neighbor in visited):
                    continue
                if(not (neighbor,city) in edges):
                    changes += 1
                visited.add(neighbor)
                dfs(neighbor)
        visited.add(0)
        dfs(0)
        return changes
