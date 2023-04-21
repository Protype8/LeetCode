class Solution:
    def totalNQueens(self, n: int) -> int:
        diagonal_1 = [False for i in range((n-1)*2+1)]
        diagonal_2 = [False for i in range((n-1)*2+1)]
        rows = [False for i in range(n)]
        res = 0
        def dfs(column):
            nonlocal res
            if(column == n):
                res+=1
            for row in range(n):
                if(not rows[row] and not diagonal_1[column+row] and not diagonal_2[column+
(n-1-row)]):
                    rows[row] = True
                    diagonal_1[column+row] = True
                    diagonal_2[column+(n-1-row)] = True
                    dfs(column+1)
                    rows[row] = False
                    diagonal_1[column+row] = False
                    diagonal_2[column+(n-1-row)] = False
        dfs(0)
        return res
