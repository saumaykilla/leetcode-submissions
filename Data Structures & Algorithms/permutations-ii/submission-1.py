class Solution:
    def permuteUnique(self, nums: List[int]) -> List[List[int]]:
        res=set()
        def backtrack(include,subset):
            if len(subset)==len(nums):
                res.add(tuple(subset.copy()))
                return
            for i in range(len(nums)):
                if not include[i]:
                    subset.append(nums[i])
                    include[i]=True
                    backtrack(include,subset)
                    subset.pop()
                    include[i] = False
        backtrack([False]*len(nums),[])
        return list(res)