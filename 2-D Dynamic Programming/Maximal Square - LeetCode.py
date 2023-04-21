class Solution:
    def maximalSquare(self, matrix: List[List[str]]) -> int:
        dp = {}
        def dfs(i,j):
            if(not i in range(len(matrix)) or not j in range(len(matrix[0])) or matrix[i][j] == 
"0"):
                return 0
            if((i,j) in dp):
                return dp[(i,j)]
            a = min(dfs(i+1,j),dfs(i,j+1),dfs(i+1,j+1))+1
            dp[(i,j)] = a
            return a
        m = 0
        for i in range(len(matrix)):
            for j in range(len(matrix[0])):
                m = max(m,dfs(i,j))
        return m*m if m != 0 else 0
