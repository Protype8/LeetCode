class Solution:
    def splitString(self, s: str) -> bool:
        def dfs(last,prev):
            if(last == len(s) and prev != int(s)):
                print(prev)
                return True
            for i in range(last,len(s)):
                cur = int(s[last:i+1])
                if(cur < prev and (abs(cur-prev) == 1 or prev == float(inf)) and dfs(i+1,cur)):
                    return True
        return dfs(0,float(inf))
