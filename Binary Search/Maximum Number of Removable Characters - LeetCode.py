class Solution:
    def isSubsequence(self,s,p,removeables):
        s_counter = 0
        p_counter = 0
        while s_counter < len(s) and p_counter < len(p):
            if(s_counter in removeables or s[s_counter] != p[p_counter]):
                s_counter += 1
            else:
                s_counter += 1
                p_counter += 1
        return p_counter == len(p)
    def maximumRemovals(self, s: str, p: str, removable: List[int]) -> int:
        l = 0
        r = len(removable)-1
        ma = 0
        while l <= r:
            m = (r+l)//2
            if(self.isSubsequence(s,p,set(removable[:m+1]))):
                ma = max(ma,m+1)
                l = m+1
            else:
                r = m-1
        return ma
