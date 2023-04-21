"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

class Solution:
    def cloneGraph(self, node: 'Node') -> 'Node':
        if(not node):
            return 
        a = {}
        visited = set([])
        def dfs(node):
            if(node == None):
                return
            a[node] = Node(node.val)
            visited.add(node.val)
            for neighbor in node.neighbors:
                if(not neighbor.val in visited):
                    dfs(neighbor)
        dfs(node)
        for org_node in a:
            for neighbor in org_node.neighbors:
                a[org_node].neighbors.append(a[neighbor])
        return a[node]
