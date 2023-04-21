class Solution:
    def numSquares(self, n: int) -> int:
        square_numbers_less_than_n = [i for i in range(1,n+1) if int(i**0.5) == i**0.5]
        dp = [math.inf for i in range(n+1)]
        dp[0] = 0
        for i in range(len(dp)):
            for c in square_numbers_less_than_n:
                if(i-c >= 0):
                    dp[i] = min(dp[i-c]+1,dp[i])
        return -1 if dp[-1] == math.inf else dp[-1]

