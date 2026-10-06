class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        if not prices:
            return 0
        l,r=0,1
        profit = 0

        while l<r and r<len(prices):
            if(prices[l]>prices[r]):
                l=r
                r+=1
            else:
                check = prices[r]-prices[l]
                profit=max(profit,check)
                r+=1
        return profit
        