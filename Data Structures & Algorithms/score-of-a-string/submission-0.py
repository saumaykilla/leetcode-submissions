class Solution:
    def scoreOfString(self, s: str) -> int:
        res=0
        for i in range(0,len(s)-1):
            firstChar=ord(s[i])
            secondChar=ord(s[i+1])
            res+=abs(firstChar-secondChar)
        return res