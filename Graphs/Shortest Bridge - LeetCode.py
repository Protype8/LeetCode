class Solution:
    def shortestBridge(self, grid: List[List[int]]) -> int:
        visited = set([])
        first_island =deque()
        for g in grid:
            print(g)
        dir = [[1,0],[0,1],[-1,0],[0,-1]]
        def find_first_island(i,j):
            if(not i in range(len(grid)) or not j in range(len(grid[0]))):
                return
            if(grid[i][j]):
                first_island.append((i,j,0))
                visited.add((i,j))
                for di,dj in dir:
                    if((i+di,j+dj) not in visited):
                        find_first_island(i+di,j+dj)
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if((i,j) not in visited and grid[i][j] and not first_island):
                    find_first_island(i,j)
        while first_island:
            i,j,steps = first_island.popleft()
            for di,dj in dir:
                if((i+di,j+dj) not in visited and i+di in range(len(grid)) and j+dj in range(len
(grid[0]))):
                    if(grid[i+di][j+dj] and (i+di,j+dj) not in visited):
                        return steps
                    first_island.append((i+di,j+dj,steps+1))
                    visited.add((i+di,j+dj))
        return 0
        

