class TreeNode:
    def __init__(self,parent=None,left=None,right=None):
        self.parent = parent
        self.descendants = []
        self.locked = 0
    def AddNode(self,node):
        self.descendants.append(node)
    def CheckForLockedDesendant(self):
        if(self.locked):
            return True
        for descandent in self.descendants:
            if(descandent.CheckForLockedDesendant()):
                return True
        return False
    def UnlockAllDesendant(self):
        for descandent in self.descendants:
            descandent.locked = 0
            descandent.UnlockAllDesendant()
class LockingTree:
    def __init__(self, parent: List[int]):
        self.nodes = {i:TreeNode(None) for i in range(len(parent))}
        for i in range(1,len(parent)):
            p = self.nodes[parent[i]]
            self.nodes[i].parent = p
            p.AddNode(self.nodes[i])
    def lock(self, num: int, user: int) -> bool:
        if(not self.nodes[num].locked):
           self.nodes[num].locked = user
           return True
        return False
    def unlock(self, num: int, user: int) -> bool:
        if(user == self.nodes[num].locked):
            self.nodes[num].locked = 0
            return True
