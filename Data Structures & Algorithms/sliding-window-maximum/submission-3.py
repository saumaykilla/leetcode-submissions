class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        l=0
        result=[]
        maxElement =-float("infinity")
        print(maxElement)
        while l<(len(nums)-k+1):
            r=l
            while r<l+k:
                maxElement=max(maxElement,nums[r])
                print(maxElement)
                r+=1
            result.append(maxElement)
            maxElement=-float("infinity")
            l+=1
        return result