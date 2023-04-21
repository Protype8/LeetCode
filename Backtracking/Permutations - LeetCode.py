class Solution:
    def permute(self, nums: List[int],res:List[int] = [],taken:Set[int] = set()) -> List[List
[int]]:
        n = []
        if(len(taken) == len(nums)):
            return [res[:]]
        for i in range(len(nums)):
            if(not i in taken):
                res.append(nums[i])
                taken.add(i)
                n += self.permute(nums,res,taken)
                taken.remove(i)
                res.pop()
        return n
