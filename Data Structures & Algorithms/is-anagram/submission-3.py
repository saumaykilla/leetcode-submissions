class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        hashMapS = dict()
        hashMapT = dict() 

        for char in s:
            hashMapS[char] = 1+ hashMapS.get(char,0)
        
        for char in t:
            hashMapT[char] = 1 + hashMapT.get(char,0)
        
        return hashMapS == hashMapT
        