class Solution:
    def makesquare(self, matchsticks: List[int]) -> bool:
        total = sum(matchsticks)
        if(total%4 != 0):
            return
        per_side = total/4
        taken = 0
        t = 0
        dp = {}
        def dfs(sides=4,current=per_side,index=0):
            nonlocal taken,t
            if((taken,sides) in dp):
                return dp[(taken,sides)]
            if(current <= 0):
                if(current == 0):
                    if(sides == 1):
                        dp[(taken,sides)] = True
                        return True
                    else:
                        dp[(taken,sides)] = dfs(sides-1,per_side,0)
                        return dp[(taken,sides)]
                dp[(taken,sides)] = False
                return False
            for i in range(index,len(matchsticks)):
                if(not taken & (1 << i)):
                    taken += (1 << i)
                    current-=matchsticks[i]
                    if(dfs(sides,current,i+1)):
                        return True
                    dp[(taken,sides)] = False
                    current+= matchsticks[i]
                    taken -= (1 << i)
        return dfs()
