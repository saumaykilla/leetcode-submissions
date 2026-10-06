class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        res =dict()

        for word in strs:
            hashSet = [0]*26

            for char in word:
                hashSet[ord(char)-ord('a')]+=1
            
            if tuple(hashSet) not in res:
                res[tuple(hashSet)]=[]

            res[tuple(hashSet)].append(word)
        
        return list(res.values())
            
        