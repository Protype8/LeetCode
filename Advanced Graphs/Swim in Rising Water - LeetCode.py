class Solution:
    def swimInWater(self, grid: List[List[int]]) -> int:
        adjDict = collections.defaultdict(list)
        dirs = [(1,0),(-1,0),(0,1),(0,-1)]
        for i in range(len(grid)):
            for j in range(len(grid)):
                for di,dj in dirs:
                    if(di+i in range(len(grid)) and dj+j in range(len(grid))):
                        adjDict[(i,j)].append((grid[di+i][dj+j],(di+i,dj+j)))
        minHeap = [(grid[0][0], (0,0))]
        visit = set()
        t = 0
        while minHeap:
            w1, n1 = heapq.heappop(minHeap)
            print(w1,n1)
            if n1 in visit:
                continue
            visit.add(n1)
            t = max(w1,t)
            if n1 == (len(grid)-1,len(grid)-1):
                break
            for w2, n2 in adjDict[n1]:
                if n2 not in visit:
                    heapq.heappush(minHeap, (w2, n2))
        return t 
