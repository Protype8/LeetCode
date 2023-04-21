class Solution:
    def integerBreak(self, n: int) -> int:
        dp = [0 for _ in range(n+1)]
        dp[1],dp[0] = 1,1
        for i in range(2,len(dp)):
            for j in range(1,(i//2)+1):
                dp[i] = max(dp[i],dp[i-j]*dp[j],(i-j)*dp[j],(i-j)*j,dp[i-j]*j)
        return dp[i]
