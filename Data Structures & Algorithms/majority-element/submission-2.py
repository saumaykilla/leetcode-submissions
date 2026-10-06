class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        hashMap = dict()

        for i in nums:
            hashMap[i] = hashMap.get(i,0) + 1

        
        sorted_hashMap = sorted(hashMap.items(), key = lambda item :[-item[1]])
        return sorted_hashMap[0][0]
        