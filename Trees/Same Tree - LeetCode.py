# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def make_tree_into_array(self,root):
        array = [None for i in range(10000)]
        def add_val(root,count):
            print(count)
            array[count] = root.val
            
            if(root.left != None):
                add_val(root.left,count*2+1)
            if(root.right != None):
                add_val(root.right,count*2+2)
        if(root != None):
            add_val(root,0)
        return array
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        return self.make_tree_into_array(p) == self.make_tree_into_array(q)
