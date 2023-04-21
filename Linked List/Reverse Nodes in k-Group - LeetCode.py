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
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        count = 1
        reverse_start = reverse_end = None
        dummyNode = ListNode(val=-1)
        dummyNode.next = head
        prev = dummyNode
        head = dummyNode.next
        while head:
            if(count == 1):
                reverse_start = head
            elif(count == k):
                reverse_end = head
                print(reverse_start.val,reverse_end.val)
                prev.next = None
                next_node = reverse_end.next
                reverse_end.next = None
