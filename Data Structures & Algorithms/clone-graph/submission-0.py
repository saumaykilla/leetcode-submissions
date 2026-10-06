"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        hashMap = {}

        def cloneMap(root):   
            if not root:
                return None         
            if root in hashMap:
                return hashMap[root]
            copy=Node(root.val)
            hashMap[root]=copy
            for i in root.neighbors:
                copy.neighbors.append(cloneMap(i))
            return copy
        return cloneMap(node)
            
        