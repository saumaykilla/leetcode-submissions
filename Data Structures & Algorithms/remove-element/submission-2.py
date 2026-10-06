class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        i=0
        n = len(nums)

        for j in range(0,n):
            if nums[j] !=val:
                nums[i] =nums[j]
                i+=1
            
        return i

            

        