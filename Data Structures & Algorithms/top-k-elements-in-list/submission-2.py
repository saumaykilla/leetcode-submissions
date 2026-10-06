class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        hashmap = dict()
        result=[]
        heap=[[] for i in range(len(nums)+1)]
        for n in nums:
            if n in hashmap:
                hashmap[n]+=1
            else:
                hashmap[n]=1
        print(hashmap)
        for i,j in hashmap.items():
            heap[j].append(i)
        print(heap)

        for i in range(len(heap)-1,0,-1):
            for j in heap[i]:
                result.append(j)
                if(len(result)==k):
                    return result

        return
        