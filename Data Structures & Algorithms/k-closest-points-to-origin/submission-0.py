class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        
        maxHeap = []

        for i in points:
            distance = math.sqrt((i[0]*i[0])+(i[1]*i[1]))
            maxHeap.append([distance,i])

        heapq.heapify(maxHeap)
        i=0
        output=[]
        while i<k:
            output.append(heapq.heappop(maxHeap)[1])
            i+=1
        return output