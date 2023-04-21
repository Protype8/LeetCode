class Solution:
    def maxAlternatingSum(self, nums: List[int]) -> int:
        dp = {}
        def dfs(i,even):
            if(i >= len(nums)):
                return 0
            if((i,even) in dp):
                return dp[(i,even)]
            take = dfs(i+1,not even)
            skip = dfs(i+1,even)
            diff = max(take+nums[i] if even else take-nums[i],skip)
            dp[(i,even)] = diff
            return diff
        return dfs(0,True)
