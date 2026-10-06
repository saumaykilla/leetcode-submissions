class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        total =0
        hashMap = {0:1}
        count = 0
        for i in nums:
            total+= i
            check = total - k
            
            count+= hashMap.get(check,0)
            
            hashMap[total]= 1 + hashMap.get(total,0)

        return count 