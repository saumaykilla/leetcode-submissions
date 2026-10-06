class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        l=r = 0

        while r<len(nums):

            while r<len(nums) and nums[r]==0:
                r+=1
            if r>=len(nums):
                break
            nums[l],nums[r]= nums[r],nums[l]
            l+=1
            r=l




