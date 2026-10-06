class Solution:
    def climbStairs(self, n: int) -> int:
        
        top=0
        second =1

        for i in range(n):
            temp = second
            second = top+second
            top = temp

        return second