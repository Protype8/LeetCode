# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> Optional[ListNode]:
        all_A_Nodes = set([])
        while headA:
            all_A_Nodes.add(headA)
            headA = headA.next
        while headB:
            if(headB in all_A_Nodes):
                return headB
            headB = headB.next
        return None
