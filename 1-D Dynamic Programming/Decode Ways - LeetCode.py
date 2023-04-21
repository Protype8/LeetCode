class Solution:
    def numDecodings(self, s: str) -> int:
        dp = [0 for i in range(len(s)+1)]
        dp[0] = 1
        for i in range(1,len(dp)):
            if(s[i-1] != "0"):
                dp[i] += dp[i-1]
            if(i > 1):
                if(s[i-2:i][0] != "0" and int(s[i-2:i]) <= 26):
                    dp[i] += dp[i-2]
        print(dp)
        return dp[-1]
