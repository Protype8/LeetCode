class Solution:
    def stoneGame(self, piles: List[int]) -> bool:
        dp = {}
        def dfs(alice_turn,l,r):
            if(l > r):
                return 0
            if (alice_turn,(l,r)) in dp:
                return dp[(alice_turn,(l,r))]
            val = piles[l]
            alice = dfs(not alice_turn,l+1,r)
            if(alice_turn):alice+=val
            val = piles[r]
            alice2 = dfs(not alice_turn,l,r-1)
            if(alice_turn):alice2+=val
            alice = max(alice,alice2)
            dp[(alice_turn,(l,r))] = alice
            return alice
        alice = dfs(True,0,len(piles)-1)
        return alice > sum(piles)-alice
            


