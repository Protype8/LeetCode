class Solution:
    def countVowelPermutation(self, n: int) -> int:
        ava = {"a":["e"],"e":["a","i"],"i":["a","e","o","u"],"o":["i","u"],"u":["a"]}
        dp = {}
        def dfs(n,selected):
            if(n == 1):
                return 1
            if((n,selected) in dp):
                return dp[(n,selected)]
            res = 0
            for i in ava[selected]:
                res += dfs(n-1,i)
            dp[(n,selected)] = res%(10**9 + 7)
            return res
        res = 0
        for vowel in ["a","e","i","o","u"]:
            res += dfs(n,vowel)
        return res%(10**9 + 7)
        
