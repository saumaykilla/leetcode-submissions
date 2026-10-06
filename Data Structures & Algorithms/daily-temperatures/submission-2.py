class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        res = [0]*len(temperatures)
        stack=[]

        for i,a in enumerate(temperatures):

            while stack and stack[-1][0]<a:
                index = stack.pop()[1]

                days = i - index
                res[index] = days
            
            stack.append((a,i))
        return res