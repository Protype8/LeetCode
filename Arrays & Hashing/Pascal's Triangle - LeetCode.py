class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        output = [[1],[1,1],[1,2,1]]
        for _ in range(3,numRows):
            new = []
            a = output[-1]
            for i in range(len(a)):
                if i == 0:
                    new.append(a[i])
                if i != len(a)-1:
                    new.append(a[i]+a[i+1])
                else:
                    new.append(a[i])
            output.append(new)
        return output[:numRows]
