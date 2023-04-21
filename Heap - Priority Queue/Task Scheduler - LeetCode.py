class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        a = [(tasks.count(i)*-1,i) for i in set(tasks)]
        heapq.heapify(a)
        process = 0
        while a:
            highest,letter = heapq.heappop(a)
            process += 1
            reserved = []
            if(highest+1 < 0):
                reserved.append((highest+1,letter))
            for i in range(n):
                if(len(a) == 0):
                    if(len(reserved) > 0):
                        process += n-i
                    break
                else:
                    h,l= heapq.heappop(a)
                    process += 1
                    if(h+1 < 0):
                        reserved.append((h+1,l))
            for r in reserved:
                heapq.heappush(a,r)
        return process
