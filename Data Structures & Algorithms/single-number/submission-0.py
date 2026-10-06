class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        hashMap=dict()

        for i in nums:
            hashMap[i]=1+hashMap.get(i,0)
        
        for i,x in hashMap.items():
            if(x==1):
                return i