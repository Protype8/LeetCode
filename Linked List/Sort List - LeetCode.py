# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeSort(self,head):
        if(not head or not head.next):
            return head
        slow, fast = head, head.next
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        second = slow.next
        slow.next = None
        list1 = self.mergeSort(head)
        list2 = self.mergeSort(second)
        dummyNode = start = ListNode()
        while list1 != None and list2 != None:
            if(list1.val < list2.val):
                dummyNode.next = list1
                list1 = list1.next
            else:
                dummyNode.next = list2
                list2 = list2.next
            dummyNode = dummyNode.next
        while list1 != None:
            dummyNode.next = list1
            list1 = list1.next
            dummyNode = dummyNode.next
        while list2 != None:
            dummyNode.next = list2
            list2 = list2.next
            dummyNode = dummyNode.next
