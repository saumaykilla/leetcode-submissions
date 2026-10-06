class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        visit=set()
        rows=len(matrix)
        cols = len(matrix[0])
        for r in range(rows):
            for c in range(cols):
                if matrix[r][c]==0:
                    visit.add((r,c))

        for r,c in visit:
            
            for column in range(cols):
                matrix[r][column]=0
            for row in range(rows):
                matrix[row][c]=0
                
