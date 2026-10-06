class Solution:
    def findMin(self, nums: List[int]) -> int:
        start=0
        end=len(nums)-1
        smallest= nums[0]

        while start<=end:

            if (nums[start]<nums[end]):
                smallest = min(smallest,nums[start])
                break
            
            mid=(start+end)//2
            smallest = min(smallest,nums[mid])
            if nums[mid]>=nums[start]:
                start=mid+1
            else:
                end=mid-1
        return smallest