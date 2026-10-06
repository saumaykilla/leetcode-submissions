class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:
        numSet = set(nums)
        currentMissing =1

        for i in numSet:
            if currentMissing in numSet:
                currentMissing+=1
        
        return currentMissing