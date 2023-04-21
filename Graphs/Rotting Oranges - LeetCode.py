class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        count_of_fresh = 0
        count_of_rotten = 0
        a = []
        for i in range(len(grid)):
            for j in range(len(grid[i])):
                if(grid[i][j] == 1):
                    count_of_fresh +=1
                if(grid[i][j] == 2):
                    a.append((i,j))
                    count_of_rotten +=1
        queue = deque([a])
        if(count_of_fresh == 0):
            return 0
        count_of_fresh += count_of_rotten
        visited = set([])
        day = 0
        while queue:
            day += 1
            a = []
            current = queue.popleft()
            for cur in current:
                grid[cur[0]][cur[1]] = 2
                count_of_fresh -= 1
                paths = [[0,1],[0,-1],[1,0],[-1,0]]
                for i,j in paths:
                    new_i,new_j = cur[0]+i,cur[1]+j
                    if(new_i in range(len(grid)) and new_j in range(len(grid[0]))):
                        if(grid[new_i][new_j] == 1 and (new_i,new_j) not in visited):
                            a.append((new_i,new_j))
                            visited.add((new_i,new_j))
            if(a):
                queue.append(a)
