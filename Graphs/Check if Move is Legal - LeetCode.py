class Solution:
    def checkMove(self, board: List[List[str]], rMove: int, cMove: int, color: str) -> bool:
        visited = set()
        for b in board:
            print(b)
        def dfs(r,c,color,dir,certain=False):
            visited.add((r,c))
            i,j = dir
            cur = "B" if color == "W" else "W"
            if(r+i in range(8) and c+j in range(8) and (r+i,c+j) not in visited and board[r+i][c
+j] != "."):
                if(certain and cur != board[r+i][c+j]):
                    return False
                if(board[r+i][c+j] == cur and not certain):
                    return True
                return dfs(r+i,c+j,board[r+i][c+j],dir)
        for i in range(-1,2):
            for j in range(-1,2):
                if(dfs(rMove,cMove,color,(i,j),True)):
                    return True
