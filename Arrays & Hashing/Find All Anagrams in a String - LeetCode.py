import string
class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:
        output = []
        p_dict = {i:p.count(i) for i in string.ascii_lowercase}
        cur = s[:len(p)]
        current_dict = {i:cur.count(i) for i in string.ascii_lowercase}
        if(current_dict == p_dict):
            output.append(0)
        
        count = 0
        for w in range(len(p),len(s)):
            current_dict[s[w]]+=1
            current_dict[s[w-len(p)]]-=1
            if(current_dict == p_dict):
                output.append(w-len(p)+1)
        return output
            
