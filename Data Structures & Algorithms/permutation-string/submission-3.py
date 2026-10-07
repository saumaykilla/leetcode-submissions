class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if len(s1) > len(s2):
            return False
        
        s1Map = {}
        s2Map = {}
        l=0
        for char in s1:
            s1Map[char] = 1 + s1Map.get(char,0)
        

        for r in range(len(s1)):
            if s2[r] in s1Map:
                s2Map[s2[r]] = 1 + s2Map.get(s2[r],0)
        
        if s1Map == s2Map:
            return True
        
        r+=1
        while r<len(s2):
            if s2[l] in s2Map:
                s2Map[s2[l]] -= 1
            l+=1
            if s2[r] in s1Map:
                s2Map[s2[r]] = 1 + s2Map.get(s2[r],0)
            r+=1
            if s1Map == s2Map:
                return True 
        return False
        