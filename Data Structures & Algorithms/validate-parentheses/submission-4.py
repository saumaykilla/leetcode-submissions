class Solution:
    def isValid(self, s: str) -> bool:
        paren = []
        valid  ={
            '(':')',
            '{':'}',
            '[':']'
        }
        for i in s:
            if i in valid:
                paren.append(valid[i])
            else:
                if not paren or paren.pop() != i:
                    return False
        return len(paren)==0
        