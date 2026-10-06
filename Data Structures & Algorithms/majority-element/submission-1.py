class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        ele=dict()
        for i in nums:
            ele[i]=ele.get(i,0)+1

        output=float("-inf")
        maxed=float("-inf")
        for i,j in ele.items():
            if j>maxed:
                output=i
                maxed=j
        return output

