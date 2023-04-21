class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        def dfs(row,column,index):
            if(index == len(word)):
                return True
            if(row < 0 or row >= len(board) or column < 0 or column >= len(board[0]) or board
[row][column] != word[index]):
                return False
            tmp = board[row][column]
            board[row][column] = "#"
            res = dfs(row+1,column,index+1) or dfs(row-1,column,index+1) or dfs(row,column+1,
index+1) or dfs(row,column-1,index+1)
            board[row][column] = tmp
            return res
        for i in range(len(board)):
            for j in range(len(board[i])):
                if(dfs(i,j,0)):
                    return True
        return False
