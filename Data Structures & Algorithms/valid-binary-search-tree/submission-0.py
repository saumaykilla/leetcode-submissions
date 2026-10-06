# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        
        def Validate(node,left,right):
            if not node:
                return True
            if not (node.val<right and left<node.val):
                return False
            
            return Validate(node.left,left,node.val) and Validate(node.right,node.val,right)
        return Validate(root,float("-infinity"),float("inf"))