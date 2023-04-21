# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def travase(self,node,prev_max):
        if(not node):
            return 0
        if(node.val >= prev_max):
            good_node = self.travase(node.left,node.val)+self.travase(node.right,node.val)+1
        else:
            good_node = self.travase(node.left,prev_max)+self.travase(node.right,prev_max)
        return good_node
    def goodNodes(self, root: TreeNode) -> int:
        return self.travase(root,float(-inf))
        
