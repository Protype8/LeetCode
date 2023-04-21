class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        all_subsets = set()
        cur = []
        def getSubset(index):
            if(index == len(nums)):
                all_subsets.add(tuple(cur[:]))
                return
            cur.append(nums[index])
            getSubset(index+1)
            cur.pop()
            getSubset(index+1)
        getSubset(0)
        return all_subsets
