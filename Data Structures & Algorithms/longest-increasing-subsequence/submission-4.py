class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        # memo ={}

        # def dfs(i,p):
        #     if i==len(nums):
        #         return 0 
        #     if (i, p) in memo:
        #         return memo[(i,p)]

        #     skip = dfs(i+1,p)
        #     take = 0
        #     if p==-1 or nums[p]<nums[i] :
        #         take = 1+ dfs(i+1,i)

        #     memo[(i,p)] = max(skip,take)

        #     return memo[(i,p)]
        
        # return dfs(0,-1)

        dp = [1]* len(nums)
        i = 0 
        while i <len(nums):
            j=0
            while j<i:
                if nums[j] <nums[i]:
                    dp[i] = max(dp[i],1+dp[j])
                j+=1
            i+=1
        
        return max(dp)




