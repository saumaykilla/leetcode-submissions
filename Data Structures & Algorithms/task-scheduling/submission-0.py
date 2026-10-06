class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        
        time=0
        hashmap= dict()
        for i in tasks:
            hashmap[i]=1+hashmap.get(i,0)

        maxHeap = [-i for i in hashmap.values()]
        heapq.heapify(maxHeap)
        q = deque()
        time = 0

        while maxHeap or q:
            time +=1
            if maxHeap:
                cnt = 1 + heapq.heappop(maxHeap)
                if cnt:
                    q.append([cnt,time+n])
            if q and q[0][1]==time:
                heapq.heappush(maxHeap,q.popleft()[0])
        return time
        