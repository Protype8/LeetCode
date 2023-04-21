class Solution:
    def findItinerary(self, tickets: List[List[str]]) -> List[str]:
        d = {}
        visited = {}
        for f,to in tickets:
            if(not f in d):
                d[f] = []
                visited[f] = []
            d[f].append(to)
            visited[f].append(False)
        for f in d:
            d[f].sort()
        cur = ["JFK"]
        def dfs(current,count):
            if(current not in d or all(visited[current])):
                if(count == len(tickets)):
                    return True
                return False
            for i in range(len(d[current])):
                cur.append(d[current][i])
                if(not visited[current][i]):
                    visited[current][i] = True
                    if(dfs(d[current][i],count+1)):
                        return cur
                    visited[current][i] = False
                cur.pop()
        return dfs("JFK",0)
            
