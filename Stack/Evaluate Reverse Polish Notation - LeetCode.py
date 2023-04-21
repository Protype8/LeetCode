class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        operations = {"+":lambda x,y:x+y,"-":lambda x,y:x-y,"*":lambda x,y:x*y,"/":lambda x,y:x/
y}
        for i in tokens:
            if(i in operations):
                num2 = stack.pop()
                num1 = stack.pop()
                got = int(operations[i](num1,num2))
                stack.append(got)
            else:
                stack.append(int(i))
        return stack[0]
        
