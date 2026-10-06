class ListNode:
    def __init__(self,val):
        self.val = val
        self.next = None

class MedianFinder:

    def __init__(self):
        self.head = ListNode(0)
        self.count = 0

    def addNum(self, num: int) -> None:
        node = ListNode(num)
        if self.count == 0:
            self.head = node
        else:
            prev=None
            dummy=self.head
            while dummy and dummy.val<num:
                prev=dummy
                dummy=dummy.next
            if prev is None:
                node.next =self.head
                self.head=node
            else:
                node.next=dummy
                prev.next=node
        self.count+=1
            
            
        
       

    def findMedian(self) -> float:
        dummy = self.head.next if self.count==0 else self.head
        if self.count % 2 !=0:
            pointer = 0
            mid = self.count //2
            while pointer <mid:
                pointer+=1
                dummy=dummy.next
            return dummy.val
        
        else:
            pointer = 0
            while pointer < (self.count //2)-1:
                pointer+=1
                dummy=dummy.next
            return (dummy.val+dummy.next.val)/2

        