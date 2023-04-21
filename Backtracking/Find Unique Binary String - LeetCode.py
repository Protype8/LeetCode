class Solution:
    def findDifferentBinaryString(self, nums: List[str]) -> str:
        l = len(nums[0])
        nums = set(nums)
        cur = ""
        def dfs(length=0):
            nonlocal cur
            if(length == l):
                if(cur not in nums):
                    return cur
                return None
            for i in ["0","1"]:
                cur = cur+i
                res = dfs(length+1)
                cur = cur[:-1]
                if(res):
                    return res
        return dfs()
