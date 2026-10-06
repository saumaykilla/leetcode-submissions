class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        word1Length = len(word1)
        word2Length = len(word2)

        i=0
        res=''
        while i<min(word1Length, word2Length):
            res+=word1[i]+word2[i]
            i+=1
        if word1Length > word2Length:
            res+=word1[i:]
        elif word2Length > word1Length:
            res+=word2[i:]
        return res 