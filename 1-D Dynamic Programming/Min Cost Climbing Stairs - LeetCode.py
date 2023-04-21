class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        one = cost[0]
        two = cost[1]
        for i in range(3,len(cost)+1):
            temp = two
            two = min(one,two)+cost[i-1]
            one = temp
        return min(one,two)
            
        
