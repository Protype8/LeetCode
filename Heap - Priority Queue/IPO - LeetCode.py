import heapq
class Solution:
    def findMaximizedCapital(self, k: int, w: int, profits: List[int], capital: List[int]) -> 
int:
        min_heap = [(capital[i],profits[i]) for i in range(len(capital))]
        k+=1
        heapq.heapify(min_heap)
        max_heap = [0]
        while max_heap and k:
            w += abs(heapq.heappop(max_heap))
            while min_heap and min_heap[0][0] <= w:
                c,p = heapq.heappop(min_heap)
                heapq.heappush(max_heap,-p)
            k-=1
        return w
