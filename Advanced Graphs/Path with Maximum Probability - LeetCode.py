class Solution:
    def maxProbability(self, n: int, edges: List[List[int]], succProb: List[float], start: int, 
end: int) -> float:
        e = collections.defaultdict(list)
        for i in range(len(edges)):
            e[edges[i][0]].append((edges[i][1], succProb[i]))
            e[edges[i][1]].append((edges[i][0], succProb[i]))
        visit = set()
        maxHeap = [[-1,start]]
        while maxHeap:
            prob, node = heapq.heappop(maxHeap)
            if node in visit:
                continue
            if(node == end):
                return abs(prob)
            visit.add(node)
            for node2, prob2 in e[node]:
                if node2 not in visit:
                    heapq.heappush(maxHeap, (prob2 * prob, node2))
        return 0
            

