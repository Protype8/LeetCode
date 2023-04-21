class Solution:
    def missingRolls(self, rolls: List[int], mean: int, n: int) -> List[int]:
        total = mean*(len(rolls)+n)
        left = total-sum(rolls)
        if(left < n):
            return []
        res = []
        while n > 0:
            take = min(6,left-(n-1))
            res.append(take)
            left-=take
            n-=1
        if(left > 0):
            return []
        else:
            return res
