class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        hashMap = dict()
        freq = [[] for i in range(len(nums)+1)]

        for i in nums:
            hashMap[i]= 1+ hashMap.get(i,0)

        for number,count in hashMap.items():
            freq[count].append(number)

        res=[]
        for i in range(len(freq)-1,0,-1):
            for num in freq[i]:
                res.append(num)
                if len(res) == k:
                    return res
        
        