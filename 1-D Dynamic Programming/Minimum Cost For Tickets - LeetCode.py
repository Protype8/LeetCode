class Solution:
    def mincostTickets(self, days: List[int], costs: List[int]) -> int:
        dp = [float(inf) for i in range(max(days)+1)]
        cost_days = [1,7,30]
        dp[0] = 0
        days = set(days)
        for i in range(1,len(dp)):
            if(i in days):
                for j in range(len(cost_days)):
                    if(i >= cost_days[j]):
                        dp[i] = min(dp[i],dp[i-cost_days[j]]+costs[j])
                    else:
                        dp[i] = min(dp[i],costs[j])
            else:
                dp[i] = dp[i-1]
        print(dp)
        return dp[-1]
