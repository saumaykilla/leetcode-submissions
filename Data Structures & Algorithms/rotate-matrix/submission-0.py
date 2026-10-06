class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        rows= len(matrix)
        cols = len(matrix[0])
        res=[]
        for c in range(0,cols):
            li = []
            for r in range(rows-1,-1,-1):
                li.append(matrix[r][c])
            res.append(li)

        for i in range(rows):
            for j in range(cols):
                matrix[i][j] =res[i][j]