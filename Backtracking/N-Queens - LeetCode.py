import copy
class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:
        diagonal_1 = [False for i in range((n-1)*2+1)]
        diagonal_2 = [False for i in range((n-1)*2+1)]
        rows = [False for i in range(n)]
        board = [["." for _ in range(n)] for _ in range(n)]
        res = []
        def dfs(column):
            if(column == n):
                a = []
                for i in range(n):
                    a.append("".join(board[i]))
                res.append(a)
            for row in range(n):
                if(not rows[row] and not diagonal_1[column+row] and not diagonal_2[column+
(n-1-row)]):
                    rows[row] = True
                    diagonal_1[column+row] = True
                    diagonal_2[column+(n-1-row)] = True
                    board[column][row] = "Q"
                    dfs(column+1)
                    rows[row] = False
                    diagonal_1[column+row] = False
                    diagonal_2[column+(n-1-row)] = False
                    board[column][row] = "."
        dfs(0)
        print(res)
        return res
