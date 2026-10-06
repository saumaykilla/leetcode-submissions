class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        prefix =1
        postfix= 1
        res = float("-inf")

        for i in range(len(nums)):
            if prefix ==0:
                prefix = 1
            
            if postfix ==0:
                postfix = 1
            
            prefix*=nums[i]
            postfix*=nums[len(nums)-1-i]

            res = max(res,prefix,postfix)
        
        return res
        