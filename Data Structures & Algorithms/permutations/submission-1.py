class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        res=[]
        def backtrack(include,subset):
            if len(subset)==len(nums):
                res.append(subset.copy())
                return
            for i in range(len(nums)):
                if not include[i]:
                    subset.append(nums[i])
                    include[i]=True
                    backtrack(include,subset)
                    subset.pop()
                    include[i] = False
        backtrack([False]*len(nums),[])
        return res
            