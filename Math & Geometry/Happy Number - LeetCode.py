class Solution:
    def isHappy(self, n: int) -> bool:
        count = 0
        while n  != 1 and count < 6:
            old_num = n
            n = 0
            while old_num > 0:
                n += ((old_num%10)**2)
                old_num = old_num//10
            count+=1
        if(n == 1):
            return True
        else:
            return False
        
