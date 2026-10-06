class Solution:
    def isValid(self, s: str) -> bool:
        bracket = {
            "(":")",
            "{":"}",
            "[":']'
        }
        stack=[]
        for ops in s:
            if ops in bracket:
                stack.append(ops)
            elif stack and ops == bracket[stack[-1]]:
                stack.pop()
            else:
                return False
        
        return True if len(stack)==0 else False