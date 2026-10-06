class Solution:
    def tribonacci(self, n: int) -> int:
        nums = [0,1,1]

        if n < 3:
            return  nums[n]

        for i in range(3,n+1):
            nums[i%3] = sum(nums)

        
        return nums[n%3]