class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        candidates.sort()
        res = []
        def getNext(target,cur,l):
            if(target <= 0):
                if(target == 0):
                    res.append(cur[:])
                return
            scanned = set()
            for i in range(l+1,len(candidates)):
                if(not candidates[i] in scanned):
                    cur.append(candidates[i])
                    getNext(target-candidates[i],cur,i)
                    scanned.add(candidates[i])
                    cur.pop()
        getNext(target,[],-1)
        return res
