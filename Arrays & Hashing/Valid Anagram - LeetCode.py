class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if(len(s) != len(t)):
            return False
        a = set(s)
        for w in a:
            if(w in t):
                if(s.count(w) !=t.count(w)):
                    return False
            else:
                return False
        return True
