class Solution:
    def minPathSum(self, grid: List[List[int]]) -> int:
        rows = len(grid)
        cols = len(grid[0])
        memo = {}
        def solve(r,c):
            if r==rows-1 and  c==cols-1:
                return grid[r][c]
            
            if r == rows or c== cols:
                return float("inf")
            
            if (r,c) in memo:
                return memo[(r,c)]

            memo[(r,c)] = grid[r][c] + min(solve(r+1,c),solve(r,c+1))

            return memo[(r,c)]




        return solve(0,0)
        