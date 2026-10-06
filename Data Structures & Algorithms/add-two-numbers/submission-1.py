# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        prev = None
        while l1:
            nextNode = l1.next
            l1.next = prev
            prev= l1
            l1= nextNode
        num1=0
        while prev:
            num1=num1*10 + prev.val
            prev=prev.next

        while l2:
            nextNode = l2.next
            l2.next = prev
            prev= l2
            l2= nextNode
        
        num2=0
        while prev:
            num2=num2*10 + prev.val
            prev=prev.next

        result = num1+num2
        if result == 0:
            return ListNode(0)
        output = ListNode(0,None)
        dummy=output

        while result >0:
            number = result%10
            result = result // 10
            dummy.next = ListNode(number)
            dummy = dummy.next
        
        return output.next
        