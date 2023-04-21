import math
class Solution:
    def restoreIpAddresses(self, s: str) -> List[str]:
        res = []
        def recursive(k,start,prefix):
            if(k == 0):
                res.append(prefix)
                return 
            cur = ""
            for i in range(start,min(start+3,len(s))):
                cur += s[i]
                if(len(s)-i-1 <= (k-1)*3 and 0 <= int(cur) <= 255 and (cur[0] != "0" or cur == 
"0")):
                    recursive(k-1,i+1,prefix+"."+cur if prefix else cur)
        recursive(4,0,"")
        return res
        
