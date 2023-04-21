class Solution:
    def intToRoman(self, num: int) -> str:
        d = {1000:"M",500:"D",100:"C",50:"L",10:"X",5:"V",1:"I"}
        vals = list(d.keys())
        ind = 0
        res = ""
        while num:
            if(num < vals[ind]):
                ind += 1
                continue
            digits = int(math.log(num, 10))+1
            first_digit =  num // 10 ** (digits - 1)
            if(first_digit == 9 or first_digit == 4):
                res += d[1*(10**(digits-1))]+d[(first_digit+1)*(10**(digits-1))]
                num -= first_digit*(10**(digits-1))
            else:
                res += d[vals[ind]]
                num -= vals[ind]
        return res
