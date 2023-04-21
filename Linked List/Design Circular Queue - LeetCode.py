class ListNode:
    def __init__(self,val,prev=None,next=None):
        self.val = val
        self.prev = prev
        self.next = next
class MyCircularQueue:
    def __init__(self, k: int):
        self.cur = self.queue_node = ListNode(-1)
        self.full = False
        current = self.cur
        for i in range(1,k):
            new = ListNode(-1,prev=current)
            current.next = new
            current = new
        current.next = self.cur
        self.cur.prev = current
    def enQueue(self, value: int) -> bool:
        if(not self.isFull()):
            self.cur.val = value
            self.cur = self.cur.next
            return True
        else:
            return False
    def deQueue(self) -> bool:
        if(not self.isEmpty()):
            self.queue_node.val = -1
            self.queue_node = self.queue_node.next
            return True
        else:
            return False
    def Front(self) -> int:
        return self.queue_node.val
    def Rear(self) -> int:
        return self.cur.prev.val
