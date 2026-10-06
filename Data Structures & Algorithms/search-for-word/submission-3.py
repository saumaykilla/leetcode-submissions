class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        rows=len(board)
        cols = len(board[0])
        visit=set()
        def backtrack(r,c,i):
            if i==len(word):
                return True
            
            if r<0 or c<0 or r>=rows or c>=cols or (r,c) in visit or word[i]!=board[r][c]:
                return False
            
            visit.add((r,c))
            res = (
                backtrack(r,c+1,i+1) or backtrack(r,c-1,i+1) or backtrack(r+1,c,i+1) or backtrack(r-1,c,i+1)
            )
            visit.remove((r,c))
            return res
        
        for r in range(rows):
            for c in range(cols):
                if backtrack(r,c,0):
                    return True
        return False
    