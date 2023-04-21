# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def travase(self,node):
        if(not node):
            return ""
        out = f"{node.val}"
        left = self.travase(node.left)
        right = self.travase(node.right)
        if(left):
            out += "("+left+")"+("("+right+")" if right else "")
        elif(right):
            out += "()"+"("+right+")"
        return out
    def tree2str(self, root: Optional[TreeNode]) -> str:
        return self.travase(root)
