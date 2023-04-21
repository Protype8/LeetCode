class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        all_subsets = []
        cur = []
        def getSubset(index):
            if(index == len(nums)):
                all_subsets.append(cur[:])
                return
            cur.append(nums[index])
            getSubset(index+1)
            cur.pop()
            getSubset(index+1)
        getSubset(0)
        return all_subsets
