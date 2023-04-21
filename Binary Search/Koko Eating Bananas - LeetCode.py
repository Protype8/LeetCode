import math
class Solution:
    def canEat(self,piles,num,h):
        for pile in piles:
            h-= math.ceil(pile/num)
        return h

    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        left = 1
        right = max(piles)
        lowest = 0
        while(left<=right):
            mid = int(left + (right - left) / 2)
            left_h = self.canEat(piles,mid,h)
            if(left_h>=0):
                right = mid - 1
            else:
                left = mid + 1
        return left
