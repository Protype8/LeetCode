class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        for i in range(9):
            in_row = []
            in_column = []
            for j in range(9):
                if(board[i][j] in in_row and board[i][j] != "."):
                    return False
                else:
                    in_row.append(board[i][j])
                if(board[j][i] in in_column and board[j][i] != "."):
                    return False
                else:
                    in_column.append(board[j][i])
        for i in range(3):
            for j in range(3):
                in_subgrid = []
                for a in range(i*3,(i+1)*3):
                    for b in range(j*3,(j+1)*3):
                        print(a,b)
                        if(board[a][b] in in_subgrid and board[a][b] != "."):
                            return False
                        else:
                            in_subgrid.append(board[a][b])
        return True
