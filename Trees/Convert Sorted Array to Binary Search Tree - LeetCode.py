# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def findMiddle(self,nums):
        if(len(nums) == 1):
            return TreeNode(val=nums[0])
        elif(len(nums) == 0):
            return None
        mid = len(nums)//2
        root = TreeNode(val=nums[mid])
        root.left = self.findMiddle(nums[:mid])
        root.right = self.findMiddle(nums[mid+1:])
        return root
    def sortedArrayToBST(self, nums: List[int]) -> Optional[TreeNode]:
        return self.findMiddle(nums)
