class Solution:
    def maxArea(self, heights: List[int]) -> int:
        left=0
        right = len(heights)-1
        result=0

        while left<right:
            area = min(heights[left],heights[right])*(right-left)
            result=max(result,area)
            if(heights[left]>heights[right]):
                right-=1
            elif(heights[right]>heights[left]):
                left+=1
            else:
                left+=1
        return result