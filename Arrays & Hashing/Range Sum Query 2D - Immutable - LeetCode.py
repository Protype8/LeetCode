class NumMatrix:

    def __init__(self, matrix: List[List[int]]):
        self.matrix = matrix
        self.prefix_sums = [[0 for i in range(len(matrix[0])+1)] for i in range(len(matrix)+1)]
        for i in range(len(matrix)):
            s = 0
            for j in range(len(matrix[0])):
                s += matrix[i][j]
                self.prefix_sums[i+1][j+1] = s+self.prefix_sums[i][j+1]
    def sumRegion(self, row1: int, col1: int, row2: int, col2: int) -> int:
       return self.prefix_sums[row2+1][col2+1]-self.prefix_sums[row2+1][col1]-self.prefix_sums
[row1][col2+1]+self.prefix_sums[row1][col1]
# Your NumMatrix object will be instantiated and called as such:
# obj = NumMatrix(matrix)
# param_1 = obj.sumRegion(row1,col1,row2,col2)
