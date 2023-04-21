class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        dp = [1 for num in nums]
        LIS = 1
        for i in range(1,len(nums)):
            counter = i
            while(counter >= 0):
                if(nums[counter] < nums[i]):
                    dp[i] = max(dp[i],dp[counter]+1)
                    LIS = max(LIS,dp[i])
                counter-=1
        return LIS
