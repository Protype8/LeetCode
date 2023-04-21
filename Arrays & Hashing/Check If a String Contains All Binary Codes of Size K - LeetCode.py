from itertools import combinations
class Solution:
    def hasAllCodes(self, s: str, k: int) -> bool:
        current = s[:k]
        all_codes = set([current])
        for i in range(k,len(s)):
            current = current[1:]+s[i]
            all_codes.add(current)
            if(len(all_codes) == 2**k):
                return True
        return False
        
