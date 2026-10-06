class Solution:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        memo={}
        def solve(i,total):
            if i==len(nums):
                if total==target:
                    return 1
                else:
                    return 0
            
            if (i,total) in memo:
                return memo[(i,total)]
            
            memo[(i,total)] = solve(i+1,total+nums[i])+ solve(i+1,total-nums[i])
            return memo[(i,total)]

        return solve(0,0)