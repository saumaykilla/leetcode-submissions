class Solution:
    def isValid(self, s: str) -> bool:
        stack=[]
        combo = {'(':")","{":"}","[":"]"}
        for i in s:

            if i in combo:
                stack.append(i)
            elif i in combo.values():
                if not stack or  combo[stack[-1]] != i:
                    return False
                stack.pop()
                

        return len(stack)==0 