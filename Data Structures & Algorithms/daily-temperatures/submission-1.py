class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        res=[0]*len(temperatures)
        stack=[]

        for i in range(len(temperatures)):
            cur = temperatures[i]
            if not stack:
                stack.append((cur,i))
            else:
                while stack and stack[-1][0]<cur:
                    temp,index = stack.pop()
                    res[index]= i-index
                stack.append((cur,i))
        return res