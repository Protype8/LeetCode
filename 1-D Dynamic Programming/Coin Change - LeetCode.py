import math
class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        dp = [math.inf for i in range(amount+1)]
        dp[0] = 0
        for i in range(len(dp)):
            for c in coins:
                if(i-c >= 0):
                    dp[i] = min(dp[i-c]+1,dp[i])
        return -1 if dp[-1] == math.inf else dp[-1]
