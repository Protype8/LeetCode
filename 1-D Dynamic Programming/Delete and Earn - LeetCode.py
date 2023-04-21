class Solution:
    def deleteAndEarn(self, nums: List[int]) -> int:
        nums.sort()
        dic = {num:0 for num in nums}
        dp = {}
        for num in nums:
            dic[num] += 1
        unique_nums = list(dic.keys())
        def dfs(index):
            if(index in dp):
                return dp[index]
            if(index >= len(unique_nums)):
                return 0
            if(index+1 <= len(unique_nums)-1 and unique_nums[index+1] == unique_nums[index]+1):
                res = max(unique_nums[index]*dic[unique_nums[index]]+dfs(index+2),dfs(index+1))
            else:
                res = unique_nums[index]*dic[unique_nums[index]]+dfs(index+1)
            dp[index] = res
            return res
        return dfs(0)
