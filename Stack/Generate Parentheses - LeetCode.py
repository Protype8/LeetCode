class Solution:
    def recursive(self,left:bool,left_count:int,right_count:int,n):
        if(left_count == n and right_count == n):
            return [")"]
        add_on = "(" if left else ")"
        l = []
        if(left_count < n):
            print(left_count,right_count,"Called left")
            for i in self.recursive(True,left_count+1,right_count,n):
                l.append(add_on+i)
        if(right_count < n):
            if(left_count > right_count):
                print(left_count,right_count,"Called right")
                for i in self.recursive(False,left_count,right_count+1,n):
                    l.append(add_on+i)
        return l
    def generateParenthesis(self, n: int) -> List[str]:
        return list(self.recursive(True,1,0,n))
        
