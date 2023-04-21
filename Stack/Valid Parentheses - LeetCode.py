class Solution:
    def isValid(self, s: str) -> bool:
        current_stack = []
        for w in s:
            if(w == "(" or w == "[" or  w =="{"):
                current_stack.append(w)
            elif(w == ")"):
                if(len(current_stack) > 0 and current_stack[-1] == "("):
                    current_stack.pop()
                else:
                    break
            elif(w == "]"):
                if(len(current_stack) > 0 and current_stack[-1] == "["):
                    current_stack.pop()
                else:
                    break
            elif(w == "}"):
                if(len(current_stack) > 0 and current_stack[-1] == "{"):
                    current_stack.pop()
                else:
                    break
        else:
            if(current_stack == []):
                return True
        return False
