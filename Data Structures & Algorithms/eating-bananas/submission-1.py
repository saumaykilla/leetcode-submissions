class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        
        l,r=1,max(piles)
        res =r
        while l<=r:
            time =0
            mid = (l+r)//2
            for count in piles:
                time+= math.ceil(float(count) / mid)

            if time<=h:
                res =mid
                r = mid -1
            else:
                l = mid +1
        
        return res
