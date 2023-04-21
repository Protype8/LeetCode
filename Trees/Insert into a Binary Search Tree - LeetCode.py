# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def insertIntoBST(self, root: Optional[TreeNode], val: int) -> Optional[TreeNode]:
        if(not root):
            return TreeNode(val)
        org = root
        while root:
            prev_root = root
            if(root.val > val):
                root = root.left
            elif(root.val < val):
                root = root.right
        if(prev_root.val < val):
            prev_root.right = TreeNode(val)
        else:
            prev_root.left = TreeNode(val)
        return org
