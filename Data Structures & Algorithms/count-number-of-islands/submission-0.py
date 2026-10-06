class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        if not grid:
            return 0
        
        islands = 0
        visit = set()
        rows = len(grid)
        cols = len(grid[0])
        def bfs(r,c):
            q=collections.deque()
            visit.add((r,c))
            q.append((r,c))
            while q:
                row,col = q.popleft()
                directions = [[1,0],[0,1],[-1,0],[0,-1]]
                for rd,cd in directions:
                    r,c = row+rd,col+cd
                    if (r in range(rows) and c in range(cols) and (r,c) not in visit and grid[r][c]=="1"):
                        visit.add((r,c))
                        q.append((r,c))

        for r in range(rows):
            for c in range(cols):
                if grid[r][c]=='1' and (r,c) not in visit:
                    islands+=1
                    bfs(r,c)
        return islands
        