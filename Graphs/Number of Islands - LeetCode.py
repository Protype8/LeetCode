class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        visited = set([])
        islands = 0
        def dfs(i,j):
            if(grid[i][j] == "1"):
                visited.add((i,j))
                if(i+1 < len(grid) and (i+1,j) not in visited):
                    dfs(i+1,j)
                if(i-1 >= 0 and (i-1,j) not in visited):
                    dfs(i-1,j)
                if(j+1 < len(grid[0]) and (i,j+1) not in visited):
                    dfs(i,j+1)
                if(j-1 >= 0 and (i,j-1) not in visited):
                    dfs(i,j-1)
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if((i,j) not in visited and grid[i][j] == "1"):
                    islands+=1
                    dfs(i,j)
        return islands
