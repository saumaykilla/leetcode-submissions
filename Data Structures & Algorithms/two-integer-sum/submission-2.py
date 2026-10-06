class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        hashSet= dict()

        for i in range(len(nums)):
            diff = target-nums[i]

            if diff in hashSet:
                return [hashSet[diff],i]
            
            hashSet[nums[i]] = i
