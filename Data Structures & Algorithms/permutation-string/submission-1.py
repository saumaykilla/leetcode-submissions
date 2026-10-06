class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if len(s1) > len(s2):
            return False

        freqMap = [0 for i in range(26)]
        freqMapS2 = [0 for i in range(26)]

        for i in s1:
            freqMap[ord(i)- ord('a')]+=1
        
        for i in range(len(s1)):
            freqMapS2[ord(s2[i])- ord('a')]+=1
        
        l=0
        r= len(s1)-1

        while r< len(s2):
            if freqMap == freqMapS2:
                return True
            freqMapS2[ord(s2[l])-ord('a')]-=1
            if r+1<len(s2):
                freqMapS2[ord(s2[r+1])- ord('a')]+=1
            l+=1
            r+=1
        
        return freqMap == freqMapS2
        