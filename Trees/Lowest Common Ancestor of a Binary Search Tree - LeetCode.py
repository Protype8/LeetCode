# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
def find(root,p,q):
    if(root == None):
        return None
    if(p.val == root.val):
        return p
    if(q.val == root.val):
        return q
    left = find(root.left,p,q)
    right = find(root.right,p,q)
    if(left and right):
        return root
    elif(left):
        return left
    elif(right):
        return right
class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        return find(root,p,q)
