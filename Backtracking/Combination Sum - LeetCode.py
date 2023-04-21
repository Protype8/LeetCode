class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        res = []
        def getNext(target,cur,l):
            if(target == 0):
                res.append(cur[:])
            if(target <= 0):
                return
            for i in range(l+1):
                cur.append(candidates[i])
                getNext(target-candidates[i],cur,i)
                cur.pop()
        getNext(target,[],len(candidates)-1)
        return res
