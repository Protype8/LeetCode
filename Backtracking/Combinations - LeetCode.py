class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        ans = []
        res = []
        def combinations(last,k):
            if(k == 0):
                ans.append(res[:])
                return
            for i in range(last+1,n-k+2):
                res.append(i)
                combinations(i,k-1)
                res.pop()
        combinations(0,k)
        return ans
