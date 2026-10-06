class Solution:
    def dailyTemperatures(self, temps: List[int]) -> List[int]:
        res =[0]*len(temps)
        stack=[]

        for i,temp in enumerate(temps):
            while stack and temp > stack[-1][0]:
                temperature,index=stack.pop()
                res[index]=(i-index)
            stack.append([temp,i])
        return res
