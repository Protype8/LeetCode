# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    sum = 0
    def f(self,node,cur):
        if(node.left):
            self.f(node.left,cur+str(node.val))
        if(node.right):
            self.f(node.right,cur+str(node.val))
        if(not node.left and not node.right):
            self.sum += int(cur+str(node.val))
    def sumNumbers(self, root: Optional[TreeNode]) -> int:
        self.f(root,"")
        return self.sum

