class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        target = sum(nums)
        if target%2!=0:
            return False
        
        target = target // 2
        memo= {}
        def dfs(i,total,target):
            if total == target:
                return True
            
            if total > target or i>=len(nums):
                return False
            
            return dfs(i+1,total+nums[i],target) or dfs(i+1,total,target)
        
        return dfs(0,0,target)
        
        