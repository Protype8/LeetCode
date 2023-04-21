"""
# Definition for a Node.
class Node:
    def __init__(self, val: int = 0, left: 'Node' = None, right: 'Node' = None, next: 'Node' = 
None):
        self.val = val
        self.left = left
        self.right = right
        self.next = next
"""
from collections import deque
class Solution:
    deque = deque()
    def travase(self):
        prev = None
        d_len = len(self.deque)
        for _ in range(0,d_len):
            node = self.deque.popleft()
            if(prev):
                prev.next = node
            prev = node
            if(node.left):
                self.deque.append(node.left)
            if(node.right):
                self.deque.append(node.right)
        if(self.deque):
            self.travase()
    def connect(self, root: 'Optional[Node]') -> 'Optional[Node]':
        if(root != None):
            self.deque.append(root)
            self.travase()
        return root
