class Solution:
    def change(self, amount: int, coins: List[int]) -> int:
        res=0
        coins.sort()
        memo ={}
        def dfs(i,total):

            if total == amount:
                return 1
            
            if total>amount or i>=len(coins):
                return 0

            if (i,total) in memo:
                return memo[(i,total)]

            take = dfs(i,total+coins[i])
            skip = dfs(i+1,total)
            memo[(i,total)]= take +skip
            return memo[(i,total)]
        
        return dfs(0,0)
            