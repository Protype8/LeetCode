class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        s_point = 0
        t_point = 0
        while t_point < len(t) and s_point < len(s):
            if(s[s_point] == t[t_point]):
                s_point += 1
            t_point+=1
        return s_point == len(s)
