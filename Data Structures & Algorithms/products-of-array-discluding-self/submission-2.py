class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        prefixCompute =[1]*len(nums)
        postfixCompute =[1]*len(nums)

        prefix =1
        postfix=1

        for i in range(0,len(nums)):
            prefixCompute[i]= prefix

            prefix *= nums[i]
        
        for i in range(len(nums)-1,-1,-1):
            postfixCompute[i]=postfix
            postfix *= nums[i]
        result =[]
        for i in range(len(nums)):
            result.append(prefixCompute[i]*postfixCompute[i])

        return result
        
        