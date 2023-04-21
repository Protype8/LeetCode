class Solution:
    def convert(self, s: str, numRows: int) -> str:
        if(numRows == 1):
            return s
        ans = ["" for i in range(numRows)]
        count = 0
        dir = 1
        for char in s:
            ans[count] += char
            count+=dir
            if(count == numRows-1):dir = -1
            elif(count == 0):dir = 1
        return "".join(ans)
