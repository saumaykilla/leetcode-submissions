"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':

        copyDict = {None:None}

        dummy=head

        while dummy:
            newNode = Node(dummy.val)
            copyDict[dummy]=newNode
            dummy=dummy.next

        dummy=head
        while dummy:
            copy = copyDict[dummy]
            copy.next =copyDict[dummy.next]
            copy.random=copyDict[dummy.random]
            dummy=dummy.next
        
        return copyDict[head]


        