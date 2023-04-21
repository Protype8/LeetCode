# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def travarse(self,node,s,k):
        if(not node):
            return False
        s += node.val
        if(s == k and node.left == None and node.right == None):
            return True
        return self.travarse(node.left,s,k) or self.travarse(node.right,s,k)
    def hasPathSum(self, root: Optional[TreeNode], targetSum: int) -> bool:
        return self.travarse(root,0,targetSum)
