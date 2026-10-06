class Solution:
    def calPoints(self, operations: List[str]) -> int:
        stack,res = [],0
        
        for i in operations:

            if i == "+":
                res+=stack[-1]+stack[-2]
                stack.append(stack[-1]+stack[-2])
                
            elif i == "C":
                res-=stack.pop()
            elif i == "D":
                res+=2*stack[-1]
                stack.append(2*stack[-1])
            else:
                res+=int(i)
                stack.append(int(i))
        
        return sum(stack)

