class Solution:
    def minimumTotal(self, triangle: List[List[int]]) -> int:
        dic = {}
        def dfs(row,index):
            if(row >= len(triangle)):
                return 0
            if((row,index) not in dic):
                dic[(row,index)] = triangle[row][index]+min(dfs(row+1,index+1),dfs(row+1,index))
            return dic[(row,index)]
        return dfs(0,0)
