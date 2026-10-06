class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        distance = []
        output=[]
        for i in points:
            x1= i[0]
            y1 = i[1]

            calc = x1*x1 + y1*y1

            distance.append((calc,x1,y1))
        heapq.heapify(distance)
        while len(output)!=k:
            val,x,y = heapq.heappop(distance)
            output.append([x,y])
        return output
