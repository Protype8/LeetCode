class TreeNode:
 def __init__(self, val=0, left=None, right=None):
     self.val = val
     self.left = left
     self.right = right
def flip(root):
    if(root == None and root == None):
        return
    temp1 = root.left
    temp2 = root.right
    root.left = temp2
    root.right = temp1
    flip(root.left)
    flip(root.right)
class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        flip(root)
        print(root)
        return root
