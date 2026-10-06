class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        length = len(nums)
        sol,ans=[],[]

        def backtrack():
            if len(sol)==length:
                ans.append(sol.copy())
                return

            for x in nums:
                if x not in sol:
                    sol.append(x)
                    backtrack()
                    sol.pop()
        
        backtrack()
        return ans