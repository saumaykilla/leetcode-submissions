class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:

        hashSet = {}
        output = []
        k = len(nums)//3
        for i in nums:
            hashSet[i] = hashSet.get(i,0)+ 1

            if i not in output and hashSet[i] >k:
                output.append(i)
        
        return output