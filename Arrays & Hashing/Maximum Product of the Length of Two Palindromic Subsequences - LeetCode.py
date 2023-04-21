from itertools import combinations,permutations
class Solution:
    def maxProduct(self, s: str) -> int:
        maximum = 0
        for i in range(1,len(s)+1):
            for a in combinations([v for v in range(len(s))],i):
                this = []
                other = []
                for i in range(len(s)):
                    if(i in a):
                        this.append(s[i])
                    else:
                        other.append(s[i])
                if(this == ["w","h","w"]):
                    print(this,other)
                for j in range(1,len(other)+1):
                    for b in combinations("".join(other),j):
                        if(this[::-1] == this and b[::-1] == b and len(this)*len(b) > maximum):
                            maximum = len(this)*len(b)
        return maximum

