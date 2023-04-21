class Solution:
    def longestIncreasingPath(self, matrix: List[List[int]]) -> int:
        dp = {}
        dirs = [(0,1),(0,-1),(1,0),(-1,0)]
        def in_range(i,j):
            return i in range(len(matrix)) and j in range(len(matrix[0]))
        def helper(i,j):
            if((i,j) in dp):
                return dp[(i,j)]
            res = 1
            for y,x in dirs:
                if(in_range(i+y,j+x) and matrix[i+y][j+x] > matrix[i][j]):
                    res = max(res,helper(i+y,j+x)+1)
            dp[(i,j)] = res
            return res
        m = 0
        for i in range(len(matrix)):
            for j in range(len(matrix[0])):
                m = max(m,helper(i,j))
        return m
