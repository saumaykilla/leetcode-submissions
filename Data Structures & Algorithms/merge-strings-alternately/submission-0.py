class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        l,r=0,0
        word=""

        for i in range(0,min(len(word1),len(word2))):
            word+=word1[l]+word2[r]
            l+=1
            r+=1

        if(len(word1)>len(word2)):
            word+=word1[l:]
        elif(len(word2)>len(word1)):
            word+=word2[r:]

        return word