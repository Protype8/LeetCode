class Solution:
    def findNumberOfLIS(self, nums: List[int]) -> int:
        dp = [1 for num in nums]
        LIS_dp = [(0,1) for num in nums]
        LIS = 1
        for i in range(1,len(nums)):
            counter = i
            count = 1
            while(counter >= 0):
                if(nums[counter] < nums[i]):
                    if(dp[counter]+1 > dp[i]):
                        dp[i] = dp[counter]+1
                        count = LIS_dp[counter][1]
                    elif(dp[counter]+1 == dp[i]):
                        count += LIS_dp[counter][1]
                    LIS = max(LIS,dp[i])
                counter-=1
            LIS_dp[i] = (dp[i],count)
        LIS_dp[0] = (1,0)
        res = 0
        for L,C in LIS_dp:
            if(L == LIS):res += C if C else 1
        return res
        
