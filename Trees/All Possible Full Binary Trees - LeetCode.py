# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def allPossibleFBT(self, n: int) -> List[Optional[TreeNode]]:
        if(n%2 == 0):
            return []
        dp = {}
        def backtrack(n):
            if n == 1:
                return [TreeNode()]
            if n in dp:
                return dp[n]
            res = []
            for l in range(1,n,2):
                r = n-1-l
                leftTrees,rightTrees = backtrack(l),backtrack(r)
                if(l == 5 and r == 5):
                    print(leftTrees == rightTrees)
                for t1 in leftTrees:
                    for t2 in rightTrees:
                        res.append(TreeNode(0,t1,t2))
            dp[n] = res
            return res
        return backtrack(n)
