from typing import List

class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        signs = ['+', '-', '*', '/']
        stack = []

        for i in tokens:
            if i not in signs:
                stack.append(int(i))
            else:
                secondNum = stack.pop()
                firstNum = stack.pop()
                
                if i == '+':
                    stack.append(firstNum + secondNum)
                elif i == '-':
                    stack.append(firstNum - secondNum)
                elif i == '*':
                    stack.append(firstNum * secondNum)
                else:  # division
                    stack.append(int(firstNum / secondNum))  # truncates toward 0

        return stack[0]  
