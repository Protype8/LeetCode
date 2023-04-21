"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        if(not head):
            return
        start = prev = Node(head.val)
        node_equalivent = {head:prev,None:None}
        f = head.next
        while f:
            new = Node(f.val)
            prev.next = new
            prev = prev.next
            node_equalivent[f] = prev
            f = f.next
        s = start
        while s:
            s.random = node_equalivent[head.random]
            s = s.next
            head = head.next
        return start
        
        
