class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        time=0
        fresh=0
        rotten = deque()
        rows=len(grid)
        cols = len(grid[0])

        for r in range(rows):
            for c in range(cols):
                if grid[r][c] ==1:
                    fresh+=1
                
                if grid[r][c] == 2:
                    rotten.append((r,c))

        
        while fresh>0 and rotten:
            level = len(rotten)

            for i in range(level):
                r,c = rotten.popleft()

                if r+1<rows and grid[r+1][c] == 1:
                    grid[r+1][c] =2
                    fresh-=1
                    rotten.append((r+1,c))
                
                if r-1>=0 and grid[r-1][c] == 1:
                    grid[r-1][c] = 2
                    fresh-=1
                    rotten.append((r-1,c))
                
                if c+1<cols and grid[r][c+1] == 1:
                    grid[r][c+1] = 2
                    fresh-=1
                    rotten.append((r,c+1))
                
                if c-1>=0 and grid[r][c-1] == 1:
                    grid[r][c-1] = 2
                    fresh-=1
                    rotten.append((r,c-1))
            time+=1
        
        return time if fresh==0 else -1
