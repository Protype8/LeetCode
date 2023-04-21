class Solution:
    def solve(self, board: List[List[str]]) -> None:
        boundary_set = set()
        for i in range(len(board)):
            boundary_set.add((i,0))
            boundary_set.add((i,len(board[0])-1))
        for j in range(len(board[0])):
            boundary_set.add((0,j))
            boundary_set.add((len(board)-1,j))
        visited = set()
        cur = set()
        def dfs(i,j):
            if(board[i][j] == "O"):
                visited.add((i,j))
                cur.add((i,j))
                if(i+1 < len(board) and (i+1,j) not in visited):
                    dfs(i+1,j)
                if(i-1 >= 0 and (i-1,j) not in visited):
                    dfs(i-1,j)
                if(j+1 < len(board[0]) and (i,j+1) not in visited):
                    dfs(i,j+1)
                if(j-1 >= 0 and (i,j-1) not in visited):
                    dfs(i,j-1)
        for i in range(len(board)):
            for j in range(len(board[0])):
                if(board[i][j] == "O" and (i,j) not in visited):
                    dfs(i,j)
                    if(len(boundary_set.intersection(cur)) == 0):
                        for c in cur:
                            board[c[0]][c[1]] = "X"
                    cur = set()
