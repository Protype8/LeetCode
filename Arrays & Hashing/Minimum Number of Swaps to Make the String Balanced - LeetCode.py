class Solution:
    def minSwaps(self, s: str) -> int:
        s =  list(s)
        reverse_s = s[::-1]
        current_stack = 0
        changes = 0
        for i in range(len(s)):
            if(s[i] == "["):
                current_stack+=1
            if(s[i] == "]"):
                if(current_stack == 0):
                    ind = len(s)-reverse_s.index("[")-1
                    s[i],s[ind] = s[ind],s[i]
                    current_stack+=1
                    changes+=1
                else:
                    current_stack -= 1
        return changes
