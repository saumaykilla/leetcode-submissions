class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        res=[]
        subset=[]
        def backtrack(n):
            if n>=len(nums):
                res.append(subset.copy())
                return
            subset.append(nums[n])
            backtrack(n+1)
            subset.pop()
            backtrack(n+1)
            
        backtrack(0)
        return res
        