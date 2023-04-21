# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
        self.max_depth = -1
def match(root,original_subRoot,subRoot):
    if subRoot == None and root == None:
        return True
    if subRoot == None or root == None:
        return False
    if(root.val == subRoot.val and subRoot.max_depth == root.max_depth):
        if(match(root.left,original_subRoot,subRoot.left) and match(root.right,original_subRoot,
subRoot.right)):
            return True
    return match(root.left,original_subRoot,original_subRoot) or match(root.right,
original_subRoot,original_subRoot)
class Solution:
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        def depth(root):
            if(root == None):
                return -1
            left_depth = depth(root.left)+1
            right_depth = depth(root.right)+1
            m = max(left_depth,right_depth)
            root.max_depth = m
            return m
        depth(subRoot)
        depth(root)
        return match(root,subRoot,subRoot)
