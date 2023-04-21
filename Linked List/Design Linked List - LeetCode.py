class Node():
    def __init__(self,val=0,next=None):
        self.val = val
        self.next = next
class MyLinkedList:
    def __init__(self):
        self.startNode = self.current = Node()
        self.len = 0
    def getNodeAtIndex(self,index):
        node = self.startNode
        for i in range(0,index):
            if(node):
                node = node.next
            else:
                break
        return node
    def get(self, index: int) -> int:
        curNode = self.getNodeAtIndex(index+1)
        return curNode.val if curNode else -1
    def addAtHead(self, val: int) -> None:
        a = self.startNode.next
        self.startNode.next  = Node(val,next=a)
        if(not a):
            self.current = self.startNode.next
        self.len+=1
    def addAtTail(self, val: int) -> None:
        self.current.next = Node(val)
        self.current = self.current.next
        self.len += 1
    def addAtIndex(self, index: int, val: int) -> None:
        if(index == self.len):
            self.addAtTail(val)
            return
        node = self.getNodeAtIndex(index)
