class Solution:
    def wordPattern(self, pattern: str, s: str) -> bool:
        di = {}
        s = s.split(" ")
        if(len(pattern) != len(s)):
            return False
        for i in range(len(pattern)):
            if(pattern[i] in di):
                if(di[pattern[i]] != s[i]):
                    return False
            else:
                if(s[i] in di.values()):
                    return False
                di[pattern[i]] = s[i]
        return True
