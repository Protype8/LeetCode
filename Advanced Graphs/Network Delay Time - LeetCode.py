class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        d = {}
        for source,target,time in times:
            l = d.get(source,[])
            l.append((target,time))
            d[source] = l 
        cost = [float(inf) for i in range(n)]
        cost[k-1] = 0
        heap = [[k,0]]
        while heap:
            i, time = heapq.heappop(heap)
            for nei,time in d.get(i,[]):
                if(time+cost[i-1] < cost[nei-1]):
                    cost[nei-1] = time+cost[i-1]
                    heapq.heappush(heap,(nei,time))
        res = max(cost)
        return res if res != float(inf) else -1
        
        

