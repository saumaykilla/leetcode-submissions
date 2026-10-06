class Solution:
    def climbStairs(self, n: int) -> int:
        
        top=1
        second =1

        for i in range(1,n):
            temp = second
            second = top+second
            top = temp

        return second