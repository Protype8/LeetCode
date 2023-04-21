class Solution:
    def partition(self, s: str) -> List[List[str]]:
        res = []
        cur = []
        def recursive(last):
            current = ""
            if(last == len(s)):
                res.append(cur[:])
            for i in range(last,len(s)):
                current += s[i]
                if(current == current[::-1]):
                    cur.append(current)
                    recursive(i+1)
                    cur.pop()
        recursive(0)
        return res
