class TrieNode:
    def __init__(self,EOW=False):
        self.words = {}
        self.EOW = EOW 
class Trie:
    def __init__(self):
        self.root = TrieNode(False)
    def insert(self, word: str) -> None:
        current = self.root
        for i in range(len(word)):
            if(not word[i] in current.words):
                current.words[word[i]] = TrieNode()
            current = current.words[word[i]]
        current.EOW = True
    def search(self, word: str) -> bool:
        current = self.root
        for i in range(len(word)):
            if(not word[i] in current.words):
                return False
            current = current.words[word[i]]
        return current.EOW
    def startsWith(self, prefix: str) -> bool:
        current = self.root
        for i in range(len(prefix)):
            if(not prefix[i] in current.words):
                return False
            current = current.words[prefix[i]]
        return True
# Your Trie object will be instantiated and called as such:
# obj = Trie()
# obj.insert(word)
# param_2 = obj.search(word)
# param_3 = obj.startsWith(prefix)
