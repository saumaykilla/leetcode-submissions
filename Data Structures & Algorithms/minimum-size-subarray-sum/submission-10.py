class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        r=0
        l=0
        curSum = 0
        res=float("inf")
        while r<len(nums):

            curSum +=nums[r]
            r+=1
            while curSum >= target:
                res = min(res,r-l)
                curSum-=nums[l]
                l+=1
            
        return 0 if res==float("inf") else res

