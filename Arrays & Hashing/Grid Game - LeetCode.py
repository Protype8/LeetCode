import math
class Solution:
    def gridGame(self, grid: List[List[int]]) -> int:
        #first_robot
        out = math.inf
        sum_two = sum(grid[0])
        sum_one = 0
        x_len = len(grid[0])
        for i in range(x_len):
            if(i-1 >= 0):
                sum_one += grid[1][i-1]
            sum_two -= grid[0][i]
            out = min(max(sum_one,sum_two),out)
            print(sum_one,sum_two)
        print(out)
        return out
