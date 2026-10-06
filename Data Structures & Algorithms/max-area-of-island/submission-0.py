class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        maxArea = 0

        if not grid:
            return maxArea

        rows= len(grid)
        cols = len(grid[0])
        visit = set()
        def bfs(r,c):
            count=1
            print(r,c)
            q=collections.deque()
            q.append((r,c))
            visit.add((r,c))

            while q:
                row,col = q.popleft()
                directions = [[-1,0],[0,1],[1,0],[0,-1]]
                for rd,cd in directions:
                    r,c = row+rd,col+cd
                    if (r in range(rows) and c in range(cols) and (r,c) not in visit and grid[r][c]==1):
                        q.append((r,c))
                        visit.add((r,c))
                        count+=1
            return count


        for r in range(rows):
            for c in range(cols):
                if grid[r][c]==1 and (r,c) not in visit:
                    c = bfs(r,c)
                    maxArea = max(c,maxArea)
        return maxArea



        
