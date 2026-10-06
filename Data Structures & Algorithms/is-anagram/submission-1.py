class Solution:
    def isAnagram(self, s: str, t: str) -> bool:

        dictOFs= dict()
        dictOFt = dict()

        for i in s:
            dictOFs[i] = dictOFs.get(i,0) + 1
        
        for i in t:
            dictOFt[i] = dictOFt.get(i,0) +1
        
        return dictOFs == dictOFt
        