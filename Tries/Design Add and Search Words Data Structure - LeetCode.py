class TrieNode:
    def __init__(self,EOW=False):
        self.words = {}
        self.EOW = EOW 
class WordDictionary:
    def __init__(self):
        self.root = TrieNode()
    def addWord(self, word: str) -> None:
        current = self.root
        for i in range(len(word)):
            if(not word[i] in current.words):
                current.words[word[i]] = TrieNode()
            current = current.words[word[i]]
        current.EOW = True
    def search(self, word: str) -> bool:
        def recursive(current,index):
            if(index == len(word)):
                return current.EOW
            if(word[index] == "."):
                for k in current.words:
                    if(recursive(current.words[k],index+1)):
                        return True
            else:
                if(word[index] in current.words):
                    return recursive(current.words[word[index]],index+1)
            return False
        return recursive(self.root,0)
# Your WordDictionary object will be instantiated and called as such:
# obj = WordDictionary()
# obj.addWord(word)
# param_2 = obj.search(word)
