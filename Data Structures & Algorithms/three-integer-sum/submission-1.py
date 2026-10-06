class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        if(len(nums)<3):
            return []
        result=[]
        nums.sort()
        for i in range(0,(len(nums)-2)):
            target= nums[i]
            start=i+1
            end = len(nums)-1
            while(start<end):
                summation = target+nums[start]+nums[end]
                if(summation==0):
                    if [target,nums[start],nums[end]] not in result:
                        result.append([target,nums[start],nums[end]])
                    start+=1
                    end-=1
                elif(summation>0):
                    end-=1
                elif(summation<0):
                    start+=1
        return result