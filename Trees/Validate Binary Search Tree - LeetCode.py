# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def Valid(self,node,lower_bound,upper_bound):
        if(not node):
            return True
        if(lower_bound < node.val < upper_bound):
            return self.Valid(node.left,lower_bound,node.val) and self.Valid(node.right,node.val,
upper_bound)
        return False
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        return self.Valid(root,float(-inf),float(inf))
