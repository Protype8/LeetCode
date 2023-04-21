# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional
[ListNode]:
        curNode =  startNode = ListNode()
        def redirectNode(node):
            nonlocal curNode
            curNode.next = node
            curNode = curNode.next
            return node.next
        while list1 and list2:
            if(list1.val < list2.val):list1 = redirectNode(list1)
            else:list2 = redirectNode(list2)
        curNode.next = list1 if list1 != None else list2
        return startNode.next
