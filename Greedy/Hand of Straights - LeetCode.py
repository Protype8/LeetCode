class Solution:
    def isNStraightHand(self, hand: List[int], groupSize: int) -> bool:
        if(len(hand)%groupSize != 0):
            return False
        hand.sort()
        m = min(hand)
        dic = {}
        for card in hand:
            dic[card] = dic.get(card,0)+1
        while dic:
            currentGroup = 0
            cur = next(iter(dic))
            while currentGroup < groupSize:
                if(not cur in dic):
                    return False
                dic[cur] -= 1
                if(dic[cur] > 0):
                    m = cur
                else:
                    del dic[cur]
                cur += 1
                currentGroup += 1
        return True
                
