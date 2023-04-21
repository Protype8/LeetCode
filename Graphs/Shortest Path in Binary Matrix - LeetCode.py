class Solution:
    def shortestPathBinaryMatrix(self, grid: List[List[int]]) -> int:
        if(grid[0][0]):
            return -1
        if(len(grid) == 1):
            return 1
        queue = deque([(0,0,1)])
        visited = set([(0,0)])
        while queue:
            x,y,steps = queue.popleft()
            for i in range(-1,2):
                for j in range(-1,2):
                    if(x+i in range(len(grid)) and y+j in range(len(grid)) and not grid[x+i][y+j]
):
                        if(x+i == len(grid)-1 and y+j == len(grid)-1):
                            return steps+1
                        queue.append((x+i,y+j,steps+1))
                        grid[x+i][y+j] = 1
        return -1

