class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        dirs = [(1,0),(-1,0),(0,1),(-1,0)]
        rows = set()
        columns = set()
        for i in range(len(matrix)):
            for j in range(len(matrix[i])):
                if(matrix[i][j] == 0):
                    rows.add(i)
                    columns.add(j)
        for row in rows:
            for j in range(len(matrix[0])):
                matrix[row][j] = 0
        for column in columns:
            for i in range(len(matrix)):
                matrix[i][column] = 0
