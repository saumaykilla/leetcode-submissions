class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        a=dict()
        for i in nums:
            if i in a:
                return True
            else:
                a[i]=1
        return False