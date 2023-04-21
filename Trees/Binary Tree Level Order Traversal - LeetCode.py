# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        dc = {}
        def travase(node,level):
            if(not node):
                return
            if(level in dc):
                dc[level].append(node.val)
            else:
                dc[level] = [node.val]
            travase(node.left,level+1)
            travase(node.right,level+1)
        travase(root,0)
        return dc.values()
