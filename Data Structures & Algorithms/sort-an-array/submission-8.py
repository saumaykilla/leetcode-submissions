class Solution:
    def sortArray(self, nums: List[int]) -> List[int]:

        def sortTwoArray(a,b,arr):
            sorted_list=[]
            i=j=k=0

            while i<len(a) and j<len(b):
                if a[i]<=b[j]:
                    arr[k]=a[i]
                    i+=1
                
                else:
                    arr[k]=b[j]
                    j+=1
                k+=1
                
            while i<len(a):
                arr[k]=a[i]
                i+=1
                k+=1
            
            while j<len(b):
                arr[k]=b[j]
                j+=1
                k+=1

        def mergeSort(arr):
            if len(arr)<=1:
                return
            
            mid=len(arr)//2
            left = arr[:mid]
            right = arr[mid:]
            mergeSort(left)
            mergeSort(right)
            sortTwoArray(left,right,arr)

        mergeSort(nums)

        return nums