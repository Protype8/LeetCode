import math
class Solution:
    def hammingWeight(self, n: int) -> int:
        if(n == 0):
            return 0
        count = 0
        for i in range(math.ceil(math.log2(n)+0.001)):
            if(n & 1<<i):
                count += 1
        return count
