class Solution:
    def findMaxForm(self, strs: List[str], m: int, n: int) -> int:
        d = {}
        dp = {}
        for a in strs:
            ones = 0
            zeros = 0
            for c in a:
                if(c == "1"):
                    ones += 1
                if(c == "0"):
                    zeros +=1
            d[a] = (ones,zeros)
        def dfs(i,zeros,ones):
            if(zeros > m or ones > n):
                return -float(inf)
            if(i == len(strs)):
                return 0
            if(i,zeros,ones) in dp:
                return dp[(i,zeros,ones)]
            s_ones,s_zeros = d[strs[i]]
            dp[(i, zeros,ones)] = max(dfs(i + 1, zeros,ones),
                                 1+dfs(i + 1,zeros+s_zeros,ones+s_ones))
            return dp[(i,zeros,ones)]
        return dfs(0,0,0)
