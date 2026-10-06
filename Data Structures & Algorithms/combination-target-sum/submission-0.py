class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        
        res=[]
        def combinationSum(i,curr,total):
            if total==target:
                res.append(curr.copy())
                return
            if i>=len(nums) or total> target:
                return

            curr.append(nums[i])

            combinationSum(i,curr,total+nums[i])

            curr.pop()

            combinationSum(i+1,curr,total)

        combinationSum(0,[],0)

        return res