class Solution:
    def isAlienSorted(self, words: List[str], order: str) -> bool:
        a = {order[i]:i for i in range(len(order))}
        max_len = max([len(word) for word in words])
        for j in range(1,len(words)):
            for i in range(0,len(words[j-1])):
                if(i >= len(words[j]) or a[words[j-1][i]] > a[words[j][i]]):
                    return False
                elif(a[words[j-1][i]] < a[words[j][i]]):
                    break
        return True
