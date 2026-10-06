# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:    
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:


        while len(lists)>1:
            list1 = lists[0]
            list2 = lists[1]
            head = ListNode(0)
            dummy=head
            while list1 and list2:
                if list1.val <=list2.val:
                    dummy.next=ListNode(list1.val)
                    list1=list1.next
                else:
                    dummy.next=ListNode(list2.val)
                    list2=list2.next
                dummy=dummy.next
            while list1:
                dummy.next=ListNode(list1.val)
                list1=list1.next
                dummy=dummy.next
            while list2:
                dummy.next = ListNode(list2.val)
                list2=list2.next
                dummy=dummy.next
            lists[1]=head.next
            lists = lists[1:]

        return lists[0] if len(lists)==1 else None


        
