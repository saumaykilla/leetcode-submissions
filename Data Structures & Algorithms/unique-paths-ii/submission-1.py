class Solution:
    def uniquePathsWithObstacles(self, obstacleGrid: List[List[int]]) -> int:
        rows = len(obstacleGrid)
        cols = len(obstacleGrid[0])

        if obstacleGrid[0][0] ==1:
            return 0
        
        
        grid = [[0 for _ in range(cols)] for _ in range(rows)]
        grid[0][0]=1
        for c in range(1,cols):
            if  obstacleGrid[0][c] ==0:
                grid[0][c] = grid[0][c-1]
        for r in range(1,rows):
            if obstacleGrid[r][0] ==0:
                    grid[r][0] = grid[r-1][0]
        
        for r in range(1,rows):
            for c in range(1,cols):
                if obstacleGrid[r][c] == 0:
                    grid[r][c] = grid[r-1][c] + grid[r][c-1]
        

        return grid[rows-1][cols-1]