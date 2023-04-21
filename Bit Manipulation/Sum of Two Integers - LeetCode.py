class Solution:
    def getSum(self, a: int, b: int) -> int:
        #Make sure a is always greater
        if(abs(a) < abs(b)):
            a,b = b,a
        a_bin = '{:011b}'.format(abs(a))
        b_bin = '{:011b}'.format(abs(b))
        negative = False
        result = ""
        carry = "0"
        if((a >= 0 and b >= 0) or (a < 0 and b < 0)):
            if(a < 0 and b < 0):
                negative = True
            for i in range(10,-1,-1):
                if(a_bin[i] == "1" and b_bin[i] == "1"):
                    result = carry + result
                    carry = "1"
                elif(a_bin[i] == "0" and b_bin[i] == "0"):
                    result = carry + result
                    carry = "0"
                else:
                    if(carry == "1"):
                        result = "0"+result
                        carry = "1"
                    else:
                        result = "1"+result
                        carry  = "0"
        else:
            for i in range(10,-1,-1):
                if(a_bin[i] == "1" and b_bin[i] == "1"):
                    result = "0"+result
                elif(a_bin[i] == "0" and b_bin[i] == "0"):
                    result = "0"+result
                elif(a_bin[i] == "1" and b_bin[i] == "0"):
