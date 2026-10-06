class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        one =0
        two =0
        zero = 0

        for i in nums:
            if i ==0:
                zero+=1
            elif i==1:
                one+=1
            elif i==2:
                two+=1

        i=0
        while zero>0:
                nums[i]=0
                zero-=1
                i+=1
        while one>0:
                nums[i]=1
                one-=1
                i+=1
        while two>0:
                nums[i]=2
                two-=1
                i+=1

        return nums
            
            



        