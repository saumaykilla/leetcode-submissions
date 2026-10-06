class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        r=0
        c=len(matrix)
        while r<c:
            endValue = matrix[r][len(matrix[r])-1]
            if target>endValue:
                r+=1
            else:
                break
        print(r)
        if r==c:
            return False
        else:
            start=0
            end=len(matrix[r])
            while start<=end:
                mid=(start+end)//2
                if matrix[r][mid]==target:
                    return True
                elif matrix[r][mid]<target:
                    start=mid+1
                else:
                    end=mid-1
            return False