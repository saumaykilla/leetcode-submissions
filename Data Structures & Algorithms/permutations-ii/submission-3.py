class Solution:
    def permuteUnique(self, nums: List[int]) -> List[List[int]]:
        res=list()
        nums.sort()
        def backtrack(include,subset):
            if len(subset)==len(nums):
                res.append(subset.copy())
                return
            for i in range(len(nums)):
                if include[i]:
                    continue
                if i>0 and nums[i]== nums[i-1] and not include[i-1]:
                    continue
                subset.append(nums[i])
                include[i] = True
                backtrack(include, subset)
                subset.pop()
                include[i] = False

        backtrack([False]*len(nums),[])
        return res