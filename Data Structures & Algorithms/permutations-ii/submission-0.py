class Solution:
    def permuteUnique(self, nums: List[int]) -> List[List[int]]:
        res=list()
        def backtrack(include,subset):
            if len(subset)==len(nums) and subset not in res:
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