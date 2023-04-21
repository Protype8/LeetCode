class Solution:
    def openLock(self, deadends: List[str], target: str) -> int:
        if("0000" in deadends):
            return -1
        if(target == "0000"):
            return 0
        visited = set()
        deadends = set(deadends)
        q = deque([("0000",0)])
        while q:
            cur,turns = q.popleft()
            for i in range(4):
                new_a  = cur[:i]+(str(int(cur[i])+1) if int(cur[i])+1 < 10 else "0")+cur[i+1:]
                if(new_a == target):
                    return turns+1
                if(new_a not in visited and new_a not in deadends):
                    q.append((new_a,turns+1))
                    visited.add(new_a)
                new_b  = cur[:i]+(str(int(cur[i])-1) if int(cur[i])-1 >= 0 else "9")+cur[i+1:]
                if(new_b == target):
                    return turns+1
                if(new_b not in visited and new_b not in deadends):
                    q.append((new_b,turns+1))
                    visited.add(new_b)
        return -1
