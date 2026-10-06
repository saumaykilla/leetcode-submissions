class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        res=""
        l,r=len(word1),len(word2)

        index = 0

        while index <l and index<r:
            res+=word1[index]+word2[index]
            index+=1
        
        while index<r:
            res+=word2[index]
            index+=1
        while index<l:
            res+=word1[index]
            index+=1
        
        return res