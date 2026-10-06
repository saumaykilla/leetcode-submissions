class Solution:   
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        self.l1 = []
        self.l2 = []

        def dfs(curr, l):
            if not curr:
                l.append('#')  # placeholder for None
                return 
            l.append(curr.val)
            dfs(curr.left, l)
            dfs(curr.right, l)

        dfs(subRoot, self.l1)
        dfs(root, self.l2)

        # sliding window
        for i in range(len(self.l2) - len(self.l1) + 1):
            if self.l2[i:i+len(self.l1)] == self.l1:
                return True
        return False
