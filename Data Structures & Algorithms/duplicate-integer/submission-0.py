class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        a=dict()
        for i in nums:
            if i in a:
                a[i]+=1
            else:
                a[i]=1
        for value in a.values():
            if(value>1):
                return True
        return False