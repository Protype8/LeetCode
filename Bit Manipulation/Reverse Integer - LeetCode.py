class Solution:
    def reverse(self, x: int) -> int:
        negative = False
        if x < 0:
            negative = True
            x = abs(x)
        revers = int(str(x)[::-1])
        revers = revers*-1 if negative else revers
        
        return 0 if revers > 2**31-1 or revers < -2**31 else revers
