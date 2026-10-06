# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        stack = []
        count=0
        dummy =ListNode(0)
        newHead=dummy

        while head:
            stack.append(head.val)
            head=head.next
            count+=1
            print(count)
            if count==k:
                print(stack)
                while len(stack)!=0:
                    element = stack[-1]
                    print(element)
                    dummy.next=ListNode(element)
                    dummy=dummy.next
                    stack=stack[:-1]
                count=0
                stack=[]
        while len(stack)!=0:
            element = stack[0]
            print(element)
            dummy.next=ListNode(element)
            dummy=dummy.next
            stack=stack[1:]
        return newHead.next
