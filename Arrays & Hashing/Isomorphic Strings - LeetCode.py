class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        a = {}
        for i in range(len(s)):
            if(s[i] in a):
                if(a[s[i]] != t[i]):
                    return False
            else:
                if(t[i] in a.values()):
                    return False
                else:
                    a[s[i]] = t[i]
        return True
