class Solution:
    def minDays(self, n: int) -> int:
        queue = deque([(n,0)])
        visited = set([])
        while queue:
            oranges,days = queue.popleft()
            visited.add(oranges)
            if(oranges == 0):
                return days
            if(oranges-1 not in visited):
                queue.append((oranges-1,days+1))
            cur = oranges//2
            if(oranges%2 == 0 and cur not in visited):
                queue.append((cur,days+1))
            cur = oranges//3
            if(oranges%3 == 0 and cur not in visited):
                queue.append((cur,days+1))
