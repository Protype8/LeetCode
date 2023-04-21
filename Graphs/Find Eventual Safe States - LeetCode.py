class Solution:
    def eventualSafeNodes(self, graph: List[List[int]]) -> List[int]:
        visited = {}
        def dfs(index):
            nonlocal visited
            if(index in visited):
                return visited[index]
            visited[index] = 0
            val = 0
            for i in graph[index]:
                val += dfs(i)
            visited[index] = 1 if val == len(graph[index]) else 0
            return visited[index]
        res = []
        for i in range(len(graph)):
            if(dfs(i)):
                res.append(i)
        return res
