# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        res = []

        q = collections.deque()
        q.append(root)

        while q:
            rightSide = None
            qLength = len(q)

            for i in range(qLength):
                node = q.popleft()
                if node:
                    rightSide = node
                    q.append(rightSide.left)
                    q.append(rightSide.right)
            
            if rightSide:
                res.append(rightSide.val)
        return res    