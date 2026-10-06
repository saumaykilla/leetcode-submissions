class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """

        n = len(nums)
        k%=n

        def rotateArray(l,r):
            while l<r:
                nums[l],nums[r] = nums[r],nums[l]
                l+=1
                r-=1
        

        rotateArray(0,n-1)
        rotateArray(0,k-1)
        rotateArray(k,n-1)

        return nums


