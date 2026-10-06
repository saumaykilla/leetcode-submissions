class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        heap = [-i for i in stones]
        heapq.heapify(heap)
        while len(heap)>1:
            firstItem = abs(heapq.heappop(heap))
            secondItem = abs(heapq.heappop(heap))
            print(firstItem,secondItem)
            result = firstItem - secondItem
    
            if result !=0:
                heapq.heappush(heap,-result)
              
        return abs(heapq.heappop(heap)) if len(heap)>0 else 0
       