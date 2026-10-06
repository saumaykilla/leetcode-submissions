class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        duplicate= dict()

        for i in nums:
            if i in duplicate:
                return True
            duplicate[i]= duplicate.get(i,0)+1
        
        return False