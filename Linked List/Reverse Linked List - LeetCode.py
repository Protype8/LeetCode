# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseNode(self,node):
        a = node.next
        if(a == None):
            return node
        if(a.next == None):
            a.next = node
            node.next = None
            return a
        new_head = self.reverseNode(a)
        node.next = None
        a.next = node
        return new_head
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if(head != None):
            new_head = self.reverseNode(head)
            return new_head
