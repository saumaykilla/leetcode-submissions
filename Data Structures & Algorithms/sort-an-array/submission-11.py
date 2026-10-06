class Solution:
    def sortArray(self, nums: List[int]) -> List[int]:
        if len(nums) <= 1:
            return nums

        mid = len(nums) // 2
        left = nums[:mid]
        right = nums[mid:]

        return self.mergeSorted(self.sortArray(left), self.sortArray(right))

    
    def mergeSorted(self,left,right):
        res=[]
        indexLeft = len(left)
        indexRight = len(right)

        i,r =0,0

        while i<indexLeft and r<indexRight:
            if left[i] < right[r]:
                res.append(left[i])
                i+=1
            else:
                res.append(right[r])
                r+=1
        
        while i< indexLeft:
            res.append(left[i])
            i+=1
        while r<indexRight:
            res.append(right[r])
            r+=1
        return res

        