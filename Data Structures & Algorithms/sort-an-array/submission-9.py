class Solution:
    def merge(self,left,right,nums):
        l,r,k =0,0,0

        while l<len(left) and r<len(right):
            if left[l]<right[r]:
                nums[k] = left[l]
                l+=1
            else:
                nums[k] = right[r]
                r+=1
            k+=1
        
        while l<len(left):
            nums[k]= left[l]
            k+=1
            l+=1
        
        while r<len(right):
            nums[k] = right[r]
            k+=1
            r+=1
        

    def sortArray(self, nums: List[int]) -> List[int]:
        if len(nums)<=1:
            return nums
        
        left = nums[:len(nums)//2]
        right = nums[len(nums)//2 :]

        self.sortArray(left)
        self.sortArray(right)
        
        self.merge(left, right, nums)
        return nums
        