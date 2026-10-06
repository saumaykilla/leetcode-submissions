class Solution:
    def appendCharacters(self, s: str, t: str) -> int:
        sLength,tLength = len(s), len(t)

        i,j=0,0
        while i<sLength and j<tLength:
            if s[i]==t[j]:
                i+=1
                j+=1
            else:
                i+=1
        
        return tLength-j
        