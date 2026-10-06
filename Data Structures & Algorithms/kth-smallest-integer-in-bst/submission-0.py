# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        self.res=[] 
        def extractValue(node):
            if node.left:
                extractValue(node.left)
            self.res.append(node.val)
            if node.right:
                extractValue(node.right)
        extractValue(root)
        return self.res[k-1]

