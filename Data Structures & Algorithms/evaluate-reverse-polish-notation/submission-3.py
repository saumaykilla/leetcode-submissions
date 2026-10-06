class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack=[]
        expressions = ["+","-","*","/"]
        for i in tokens:
            if i not in expressions:
                stack.append(i)
            else:
                num2=stack.pop()
                num1=stack.pop()
                val=eval(str(num1)+str(i)+str(num2))
                stack.append(int(val))
        return int(stack.pop())