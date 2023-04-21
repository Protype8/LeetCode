class Solution:
    def countSubIslands(self, grid1: List[List[int]], grid2: List[List[int]]) -> int:
        cur = set([])
        visited = set([])
        islands = 0
        def dfs(i,j):
            cur.add((i,j))
            res = True
            if(i+1 < len(grid2) and (i+1,j) not in cur and grid2[i+1][j]):
                dfs(i+1,j)
            if(i-1 >= 0 and (i-1,j) not in cur and grid2[i-1][j]):
                dfs(i-1,j)
            if(j+1 < len(grid2[0]) and (i,j+1) not in cur and grid2[i][j+1]):
                dfs(i,j+1)
            if(j-1 >= 0 and (i,j-1) not in cur and grid2[i][j-1]):
                dfs(i,j-1)
            return res
        for i in range(0,len(grid2)):
            for j in range(0,len(grid2[0])):
                if(grid2[i][j] and (i,j) not in visited and dfs(i,j)):
                    visited.update(cur)
                    for c in cur:
                        if(not grid1[c[0]][c[1]]):
                            break
                    else:
                        islands+=1
                cur = set([])
        return islands
