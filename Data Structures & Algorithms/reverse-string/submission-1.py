class Solution:
    def reverseString(self, s: List[str]) -> None:
        """
        Do not return anything, modify s in-place instead.
        """
        for i in range(0,len(s)//2):
            cur=s[len(s)-1-i]
            s[len(s)-1-i]=s[i]
            s[i]=cur