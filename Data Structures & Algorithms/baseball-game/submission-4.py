class Solution:
    def calPoints(self, operations: List[str]) -> int:
        stack = []

        for i in operations:

            if i=="+" and len(stack)>=2:
                stack.append(int(stack[-1])+int(stack[-2]))
            
            elif i=="C" and stack:
                stack.pop()
            elif i=="D" and stack:
                stack.append(int(stack[-1])*2)
            else:
                stack.append(i)
        output=0
        for i in stack:
            output+=int(i)
        return output
        