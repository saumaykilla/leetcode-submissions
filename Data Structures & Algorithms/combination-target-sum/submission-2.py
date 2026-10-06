class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        res=[]
        subset=[]

        def backtrack(i,cur):
            if cur>target or i>=len(nums):
                return
            if cur==target:
                res.append(subset.copy())
                return
            subset.append(nums[i])
            backtrack(i,cur+nums[i])
            subset.pop()
            backtrack(i+1,cur)
        backtrack(0,0)
        return res
        