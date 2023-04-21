class Solution:
    def climbStairs(self, n: int) -> int:
        s = [0 for _ in range(n+1)]
        s[1] = 1
        try:
            s[2] = 2
        except:
            pass
        for i in range(3,n+1):
            s[i] += s[i-1]
            s[i] += s[i-2]
        print(s)
        return s[-1]
